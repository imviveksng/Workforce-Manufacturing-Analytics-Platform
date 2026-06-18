import pandas as pd

def extract_data():

    employees = pd.read_excel(
        "data/employees.xlsx"
    )

    attendance = pd.read_excel(
        "data/attendance.xlsx"
    )

    overtime = pd.read_excel(
        "data/overtime.xlsx"
    )

    production = pd.read_excel(
        "data/production.xlsx"
    )

    quality = pd.read_excel(
        "data/quality.xlsx"
    )

    return {
        "employees": employees,
        "attendance": attendance,
        "overtime": overtime,
        "production": production,
        "quality": quality
    }

data = extract_data()

employees_df = data["employees"]
attendance_df = data["attendance"]
overtime_df = data["overtime"]