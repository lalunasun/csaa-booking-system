from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


OUTPUT = Path(__file__).with_name("csaa_data_import_template_example.xlsx")


SHEETS = {
    "00_Instructions": [
        ["Section", "Notes"],
        ["How to use", "Fill each sheet from row 2 onward. Keep column names unchanged."],
        ["Do not merge", "Do not merge cells. Use one row per parent, student, class, or enrollment."],
        ["Unique keys", "parent_username must be unique. student_name is matched together with parent_username."],
        ["Import order", "Terms, Rooms, Time_Slots, Categories, Courses, Parents, Students, Lesson_Schedule, Enrollment_Final."],
        ["Sensitive data", "Use demo data for students. Do not share production phone/email data with student contributors."],
        ["Final course table", "Enrollment_Final is the child's final class registration table. Keep it separate from Student_Info."],
    ],
    "Parent_Info": [
        ["parent_username", "parent_name", "phone", "email", "password", "address", "class_pass_enabled", "notes"],
        ["parent_001", "Amy Chen", "416-555-0101", "amy.chen@example.com", "Temp1234", "Toronto", "no", "Demo parent with one child"],
        ["parent_002", "Brian Li", "416-555-0102", "brian.li@example.com", "Temp1234", "Markham", "yes", "Has class pass permission"],
    ],
    "Student_Info": [
        ["parent_username", "student_name", "preferred_name", "age", "gender", "phone", "email", "notes"],
        ["parent_001", "Alice Chen", "Alice", 8, "F", "", "", "Robotics beginner"],
        ["parent_002", "Ethan Li", "Ethan", 9, "M", "", "", "May use class pass"],
        ["parent_002", "Ivy Li", "Ivy", 7, "F", "", "", "Sibling of Ethan"],
    ],
    "Term_Info": [
        ["term_name", "start_date", "end_date", "status", "notes"],
        ["2026 Summer", "2026-06-28", "2026-08-31", "active", "Summer regular term"],
        ["2026 Fall", "2026-09-08", "2026-12-20", "planned", "Fall term"],
    ],
    "Room_Info": [
        ["room_name", "capacity", "teacher_name", "notes"],
        ["Room1", 4, "Teacher A", "Robotics room"],
        ["Room2", 4, "Teacher B", "Coding room"],
        ["Room3", 4, "Teacher C", ""],
    ],
    "Time_Slots": [
        ["time_label", "start_time", "end_time", "duration_minutes", "day_type", "notes"],
        ["16:00-17:00", "16:00", "17:00", 60, "weekday", "Tue-Fri"],
        ["17:00-18:00", "17:00", "18:00", 60, "weekday", "Tue-Fri"],
        ["09:00-10:00", "09:00", "10:00", 60, "weekend", "Sat/Sun"],
        ["Trial 90min", "10:00", "11:30", 90, "trial", "Trial uses 1 classroom slot"],
    ],
    "Category_Info": [
        ["category_name", "notes"],
        ["Robotics", "Robot and engineering classes"],
        ["Coding", "Programming classes"],
        ["Game Design", "Roblox/Scratch style classes"],
    ],
    "Course_Info": [
        ["class_name", "category_name", "default_price", "default_capacity", "is_trial_available", "is_active", "image_file_name", "description"],
        ["Creator", "Robotics", 40, 4, "yes", "yes", "creator.png", "Intro robotics class"],
        ["Wedo", "Robotics", 40, 4, "yes", "yes", "wedo.png", "Robotics class"],
        ["Python", "Coding", 40, 4, "yes", "yes", "python.png", "Python coding"],
        ["Roblox", "Game Design", 40, 4, "no", "yes", "roblox.png", "Roblox design"],
    ],
    "Lesson_Schedule": [
        ["class_name", "term_name", "day_of_week", "time_label", "room_name", "teacher_name", "capacity", "start_date", "end_date", "notes"],
        ["Creator", "2026 Summer", "Tuesday", "16:00-17:00", "Room1", "Teacher A", 4, "2026-06-28", "2026-08-31", "Regular weekly class"],
        ["Wedo", "2026 Summer", "Tuesday", "16:00-17:00", "Room2", "Teacher B", 4, "2026-06-28", "2026-08-31", "Regular weekly class"],
        ["Python", "2026 Summer", "Thursday", "18:00-19:00", "Room3", "Teacher C", 4, "2026-06-28", "2026-08-31", "Regular weekly class"],
    ],
    "Enrollment_Final": [
        ["parent_username", "student_name", "class_name", "term_name", "day_of_week", "time_label", "room_name", "lesson_count", "price", "payment_status", "order_status", "start_date", "end_date", "notes"],
        ["parent_001", "Alice Chen", "Creator", "2026 Summer", "Tuesday", "16:00-17:00", "Room1", 10, 400, "paid", "scheduled", "2026-06-28", "2026-08-31", "Final class registration"],
        ["parent_002", "Ethan Li", "Python", "2026 Summer", "Thursday", "18:00-19:00", "Room3", 10, 400, "pending", "pending_admin", "2026-06-28", "2026-08-31", "Admin needs payment confirmation"],
    ],
    "Trial_Registration": [
        ["parent_username", "student_name", "robotics_class", "robotics_date", "robotics_time", "coding_class", "coding_date", "coding_time", "status", "notes"],
        ["parent_002", "Ivy Li", "Creator", "2026-07-07", "Trial 90min", "Python", "2026-07-09", "Trial 90min", "scheduled", "Trial package: robotics + coding"],
    ],
    "Class_Pass": [
        ["parent_username", "student_name", "pass_name", "total_sessions", "used_sessions", "remaining_sessions", "start_date", "expiry_date", "status", "notes"],
        ["parent_002", "Ethan Li", "10-Class Pass", 10, 1, 9, "2026-07-01", "2026-12-31", "active", "Parent can request class time"],
    ],
    "Class_Pass_Booking": [
        ["parent_username", "student_name", "class_name", "booking_date", "time_label", "room_name", "status", "notes"],
        ["parent_002", "Ethan Li", "Wedo", "2026-07-14", "16:00-17:00", "Room2", "requested", "Waiting for admin confirmation"],
    ],
    "Adjustment_History": [
        ["parent_username", "student_name", "original_class", "original_date", "original_time", "new_class", "new_date", "new_time", "adjustment_type", "status", "reason", "notes"],
        ["parent_001", "Alice Chen", "Creator", "2026-07-07", "16:00-17:00", "Wedo", "2026-07-08", "16:00-17:00", "sick_leave", "makeup_available", "Sick", "Demo makeup record"],
    ],
    "Comments_History": [
        ["parent_username", "student_name", "class_name", "lesson_date", "teacher_name", "comment", "created_time"],
        ["parent_001", "Alice Chen", "Creator", "2026-07-07", "Teacher A", "Worked well with gears and followed instructions.", "2026-07-07 17:10"],
    ],
}


def style_sheet(ws):
    header_fill = PatternFill("solid", fgColor="D9EAF7")
    required_fill = PatternFill("solid", fgColor="FFF2CC")
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)
    for idx, column_cells in enumerate(ws.columns, start=1):
        max_len = 12
        for cell in column_cells:
            value = "" if cell.value is None else str(cell.value)
            max_len = max(max_len, min(len(value) + 2, 42))
        ws.column_dimensions[get_column_letter(idx)].width = max_len
    ws.freeze_panes = "A2"
    if ws.max_row > 1:
        ws.auto_filter.ref = ws.dimensions
    if ws.title in {"Parent_Info", "Student_Info", "Enrollment_Final"}:
        for cell in ws[1]:
            if cell.value in {"parent_username", "student_name", "class_name", "term_name"}:
                cell.fill = required_fill


def main():
    wb = Workbook()
    wb.remove(wb.active)
    for title, rows in SHEETS.items():
        ws = wb.create_sheet(title)
        for row in rows:
            ws.append(row)
        style_sheet(ws)
    wb.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
