from faker import Faker
import pandas as pd
import random

fake = Faker()

departments = [
    "Production",
    "Quality",
    "Stores",
    "Maintenance",
    "HR",
    "Finance"
]

designations = [
    "Operator",
    "Senior Operator",
    "Supervisor",
    "Engineer",
    "Executive"
]

employees = []

for i in range(1,1001):

    employees.append({

        "emp_id":f"E{i:04}",

        "emp_name":fake.name(),

        "department":random.choice(departments),

        "designation":random.choice(designations),

        "joining_date":fake.date_between(
            start_date="-5y",
            end_date="today"
        ),

        "salary":random.randint(
            20000,
            100000
        )

    })

df = pd.DataFrame(employees)

df.to_excel(
    "data/employees.xlsx",
    index=False
)

print("Employee file created")