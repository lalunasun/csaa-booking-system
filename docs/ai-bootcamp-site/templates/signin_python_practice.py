"""
Pure Python sign-in/out practice.

Goal:
Students learn how a simple front-desk sign-in / sign-out action becomes structured data.
No web framework is needed for this exercise.
"""

import csv
from datetime import datetime
from pathlib import Path


STUDENTS = [
    {"student_id": "S001", "first_name": "Emma", "last_name": "Chen", "room": "Room 2"},
    {"student_id": "S002", "first_name": "Liam", "last_name": "Wong", "room": "Room 4"},
    {"student_id": "S003", "first_name": "Olivia", "last_name": "Smith", "room": "Room 1"},
]

OUTPUT_FILE = Path("attendance_output.csv")


def normalize_name(value):
    """Clean text so ' Emma ', 'emma', and 'EMMA' can match the same student."""
    return value.strip().lower()


def find_student(first_name, last_name):
    clean_first = normalize_name(first_name)
    clean_last = normalize_name(last_name)

    for student in STUDENTS:
        if (
            normalize_name(student["first_name"]) == clean_first
            and normalize_name(student["last_name"]) == clean_last
        ):
            return student

    return None


def write_attendance_record(student, action):
    record = {
        "student_id": student["student_id"],
        "student_name": f"{student['first_name']} {student['last_name']}",
        "room": student["room"],
        "action": action,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    file_exists = OUTPUT_FILE.exists()
    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=record.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(record)

    return record


def main():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    action = input("Action, sign_in or sign_out: ").strip().lower()

    if action not in {"sign_in", "sign_out"}:
        print("Please type sign_in or sign_out.")
        return

    student = find_student(first_name, last_name)
    if student is None:
        print("Student not found. Please check the spelling.")
        return

    record = write_attendance_record(student, action)
    print(f"{record['student_name']} should go to {record['room']}.")
    print(f"{action} saved to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
