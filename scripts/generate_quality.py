import pandas as pd
import random

production = pd.read_excel(
    "data/production.xlsx"
)

quality_data = []

for _, row in production.iterrows():

    units_checked = row["units_produced"]

    rejection_rate = random.uniform(
        0.01,
        0.05
    )

    rejected_units = round(
        units_checked * rejection_rate
    )

    defect_percentage = round(
        (rejected_units / units_checked) * 100,
        2
    )

    quality_data.append([

        row["production_date"],
        row["department"],
        row["machine_id"],

        units_checked,
        rejected_units,
        defect_percentage

    ])

quality_df = pd.DataFrame(

    quality_data,

    columns=[

        "quality_date",
        "department",
        "machine_id",

        "units_checked",
        "rejected_units",
        "defect_percentage"

    ]

)

quality_df.to_excel(

    "data/quality.xlsx",

    index=False

)

print(quality_df.shape)