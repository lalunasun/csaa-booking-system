import pandas as pd

df = pd.read_csv("../data/attendance.csv")

print("First rows:")
print(df.head())

total_records = len(df)
status_counts = df["status"].value_counts()

print("\nTotal records:", total_records)
print("\nStatus counts:")
print(status_counts)

absent_count = status_counts.get("absent", 0)
absence_rate = absent_count / total_records

print("\nAbsence rate:", round(absence_rate, 2))

room_counts = df.groupby("room")["student_id"].count()

print("\nRecords by room:")
print(room_counts)
