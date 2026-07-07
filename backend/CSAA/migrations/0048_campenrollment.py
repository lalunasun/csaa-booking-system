from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSAA', '0047_campattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampEnrollment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled'), ('waitlist', 'Waitlist')], default='active', max_length=20)),
                ('payment_status', models.CharField(choices=[('unpaid', 'Unpaid'), ('deposit', 'Deposit'), ('paid', 'Paid'), ('waived', 'Waived')], default='unpaid', max_length=20)),
                ('note', models.TextField(blank=True, default='', max_length=1000)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('default_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='camp_enrollments', to='CSAA.tag')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_enrollments', to='CSAA.user')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_enrollments', to='CSAA.child')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_enrollments', to='CSAA.term')),
            ],
            options={
                'db_table': 'b_camp_enrollment',
                'indexes': [models.Index(fields=['term', 'status'], name='b_camp_enr_term_status_idx'), models.Index(fields=['student', 'term'], name='b_camp_enr_student_term_idx')],
                'constraints': [models.UniqueConstraint(fields=('student', 'term'), name='unique_camp_enrollment_student_term')],
            },
        ),
    ]
