import pandas as pd
import random

dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31"
)

machine_department = {
    "M001":"Production",
    "M002":"Production",
    "M003":"Production",
    "M004":"Production",
    "M005":"Production",
    "M006":"Production",
    "M007":"Production",
    "M008":"Production",
    "M009":"Production",
    "M010":"Production"
}

production_data = []

for date in dates:

    for machine in machine_department:

        for hour in range(24):

            units_produced = random.randint(
                20,
                60
            )

            department = machine_department[machine]

            production_data.append([

                date,
                department,
                machine,
                hour,
                units_produced

            ])

production_df = pd.DataFrame(

    production_data,

    columns=[
        "production_date",
        "department",
        "machine_id",
        "hour",
        "units_produced"
    ]

)

production_df.to_excel(

    "data/production.xlsx",

    index=False

)

print(f"Data generation complete. Shape: {production_df.shape}")