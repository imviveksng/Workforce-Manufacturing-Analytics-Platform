import pandas as pd
import random

employees = pd.read_excel(
    "data/employees.xlsx"
)

dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31"
)

attendance_data = []

for emp in employees["emp_id"]:

    for date in dates:

        status = random.choices(
            ["Present",
             "Absent",
             "Leave"],
            weights=[90,5,5]
        )[0]

        shift = random.choice(
            ["A","B","C"]
        )

        attendance_data.append([
            emp,
            date,
            status,
            shift
        ])

attendance_df = pd.DataFrame(

    attendance_data,

    columns=[
        "emp_id",
        "attendance_date",
        "status",
        "shift"
    ]

)

attendance_df.to_excel(

    "data/attendance.xlsx",

    index=False

)

print(attendance_df.shape)