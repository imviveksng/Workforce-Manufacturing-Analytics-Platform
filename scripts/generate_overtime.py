import pandas as pd
import random

attendance = pd.read_excel(
    "data/attendance.xlsx"
)

present_df = attendance[
    attendance["status"] == "Present"
]

ot_data = []

for _, row in present_df.iterrows():

    if random.random() < 0.30:

        ot_hours = random.randint(
            1,
            6
        )

        ot_data.append([
            row["emp_id"],
            row["attendance_date"],
            ot_hours
        ])

overtime_df = pd.DataFrame(

    ot_data,

    columns=[
        "emp_id",
        "ot_date",
        "ot_hours"
    ]

)

overtime_df.to_excel(

    "data/overtime.xlsx",

    index=False

)

print(overtime_df.shape)