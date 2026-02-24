import pandas as pd
import random

classes = ["MCA", "MBA", "CSE", "AIDS"]
students_per_class = 60

data = []

roll_base = {
    "MCA": 1000,
    "MBA": 2000,
    "CSE": 3000,
    "AIDS": 4000
}

for cls in classes:
    for i in range(1, students_per_class + 1):

        roll_no = roll_base[cls] + i

        attendance = random.randint(30, 100)
        study_hours = round(random.uniform(0.3, 5.0), 1)
        internal = random.randint(30, 100)
        assignment = random.randint(30, 100)
        previous = random.randint(30, 100)

        avg = (internal + assignment + previous) / 3

        if avg >= 80 and attendance >= 75:
            grade = "A"
        elif avg >= 65:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "Fail"

        data.append([
            roll_no, cls, attendance, study_hours,
            internal, assignment, previous, grade
        ])

df = pd.DataFrame(data, columns=[
    "RollNo", "Class", "Attendance", "StudyHours",
    "InternalMarks", "Assignment", "PreviousSem", "FinalGrade"
])

df.to_csv("data/student_data.csv", index=False)

print("Dataset with 240 students created successfully!")
