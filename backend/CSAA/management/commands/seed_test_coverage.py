import datetime

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from CSAA.models import (
    CampAttendance,
    CampEnrollment,
    CampWaiver,
    Child,
    ClassPass,
    ClassPassBooking,
    Lesson,
    StudentAttendance,
    StudentComment,
    Tag,
    Term,
    Thing,
    User,
)


class Command(BaseCommand):
    help = "Add idempotent local demo data for newer workflow testing."

    def _admin(self):
        admin = User.objects.filter(username="test", role="0").first()
        if not admin:
            raise CommandError("Admin user test does not exist.")
        return admin

    def _child(self, username, fallback_name=None):
        child = Child.objects.filter(parent__username=username).select_related("parent").first()
        if not child and fallback_name:
            child = Child.objects.filter(name=fallback_name).select_related("parent").first()
        if not child:
            raise CommandError(f"Child for {username} does not exist.")
        return child

    def _thing(self, title, day, time):
        thing = (
            Thing.objects.filter(title=title, day=day, time__time=time, status="0")
            .select_related("time", "tag")
            .first()
        )
        if not thing:
            raise CommandError(f"Missing class: {title} {day} {time}")
        Lesson.objects.get_or_create(thing=thing)
        return thing

    def _lesson(self, thing):
        lesson, _ = Lesson.objects.get_or_create(thing=thing)
        return lesson

    def _ensure_class_pass_data(self, admin):
        child = self._child("parent_32")
        class_pass, _ = ClassPass.objects.update_or_create(
            parent=child.parent,
            child=child,
            title="Class Pass",
            defaults={
                "total_sessions": 20,
                "used_sessions": 1,
                "valid_from": datetime.date(2026, 7, 10),
                "valid_until": datetime.date(2026, 12, 31),
                "status": "active",
                "note": "Demo pass card for parent_32 workflow testing.",
                "created_by": admin,
            },
        )

        booking_specs = [
            ("Creator", "Tue", "16:00-17:00", datetime.date(2026, 7, 21), "pending"),
            ("Creator", "Wed", "16:00-17:00", datetime.date(2026, 7, 22), "approved"),
            ("Python", "Thu", "18:00-19:00", datetime.date(2026, 7, 23), "completed"),
        ]
        for title, day, time, requested_date, status in booking_specs:
            thing = self._thing(title, day, time)
            booking_defaults = {
                "parent": child.parent,
                "child": child,
                "parent_note": f"Demo {status} class pass request.",
                "status": status,
                "admin_note": "Created by seed_test_coverage.",
            }
            if status in ["approved", "completed"]:
                booking_defaults.update(
                    {
                        "target_lesson": self._lesson(thing),
                        "reviewed_by": admin,
                        "reviewed_time": timezone.now(),
                    }
                )
            if status == "completed":
                booking_defaults.update(
                    {
                        "completed_by": admin,
                        "completed_time": timezone.now(),
                    }
                )
            ClassPassBooking.objects.update_or_create(
                class_pass=class_pass,
                requested_class=thing,
                requested_date=requested_date,
                defaults=booking_defaults,
            )

    def _ensure_attendance_and_comments(self, admin):
        samples = [
            ("schedule_demo_parent_01", "Alice Demo", "Creator", "Tue", "16:00-17:00", datetime.date(2026, 6, 23), False),
            ("schedule_demo_parent_03", "Chloe Demo", "Creator", "Tue", "16:00-17:00", datetime.date(2026, 6, 23), True),
            ("schedule_demo_parent_04", "Daniel Demo", "Wedo", "Sun", "10:00-11:00", datetime.date(2026, 6, 28), True),
            ("parent_32", None, "Python", "Thu", "18:00-19:00", datetime.date(2026, 7, 23), False),
        ]
        for username, fallback_name, title, day, time, lesson_date, is_absent in samples:
            child = self._child(username, fallback_name)
            lesson = self._lesson(self._thing(title, day, time))
            StudentAttendance.objects.update_or_create(
                student=child,
                lesson=lesson,
                lesson_date=lesson_date,
                defaults={"is_absent": is_absent, "marked_by": admin},
            )

        parent_32_child = self._child("parent_32")
        lesson = self._lesson(self._thing("Python", "Thu", "18:00-19:00"))
        comments = [
            "Good focus during Python practice. Needs more debugging repetition.",
            "Completed the loop activity with help from the teacher.",
            "Can explain variables clearly. Next step: use functions independently.",
            "Strong participation. Please review file reading before next lesson.",
        ]
        for index, content in enumerate(comments, 1):
            StudentComment.objects.update_or_create(
                student=parent_32_child,
                lesson=lesson,
                lesson_date=datetime.date(2026, 7, 23) + datetime.timedelta(days=index),
                defaults={"content": content, "created_by": admin},
            )

    def _ensure_camp_data(self):
        camp_term = Term.objects.filter(title="2026 Summer Camp Week 1").first()
        if not camp_term:
            return
        room = Tag.objects.filter(title="Room1").first()
        enrollments = CampEnrollment.objects.filter(term=camp_term).select_related("student", "parent")
        for enrollment in enrollments:
            CampWaiver.objects.update_or_create(
                student=enrollment.student,
                parent=enrollment.parent,
                term=camp_term,
                waiver_version="2026-summer-v1",
                defaults={
                    "signer_name": enrollment.parent.nickname or enrollment.parent.username,
                    "signed_ip": "127.0.0.1",
                },
            )

        for enrollment, status in zip(enrollments[:2], ["signed_in", "signed_out"]):
            defaults = {
                "room": enrollment.default_room or room,
                "status": status,
                "sign_in_time": timezone.now(),
                "note": "Created by seed_test_coverage.",
            }
            if status == "signed_out":
                defaults["sign_out_time"] = timezone.now()
            CampAttendance.objects.update_or_create(
                student=enrollment.student,
                term=camp_term,
                attendance_date=datetime.date(2026, 7, 15),
                defaults=defaults,
            )

    @transaction.atomic
    def handle(self, *args, **options):
        admin = self._admin()
        self._ensure_class_pass_data(admin)
        self._ensure_attendance_and_comments(admin)
        self._ensure_camp_data()
        self.stdout.write(self.style.SUCCESS("Extended test coverage data is ready."))
