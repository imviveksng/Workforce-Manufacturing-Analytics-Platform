import pandas as pd

def clean_employees(df):

    df = df.drop_duplicates()

    df = df.dropna(
        subset=["emp_id"]
    )

    return df

def clean_attendance(df):

    df = df.drop_duplicates()

    valid_status = [
        "Present",
        "Absent",
        "Leave"
    ]

    valid_shift = [
        "A",
        "B",
        "C"
    ]

    df = df[
        df["status"].isin(valid_status)
    ]

    df = df[
        df["shift"].isin(valid_shift)
    ]

    return df

def clean_overtime(df):

    df = df.drop_duplicates()

    df = df[
        df["ot_hours"] > 0
    ]

    df = df[
        df["ot_hours"] <= 12
    ]

    return df

def clean_production(df):

    df = df.drop_duplicates()

    df = df[
        df["units_produced"] >= 0
    ]

    return df

def clean_quality(df):

    df = df.drop_duplicates()

    df = df[
        df["rejected_units"] >= 0
    ]

    return df

def transform_data(data):

    employees = clean_employees(
        data["employees"]
    )

    attendance = clean_attendance(
        data["attendance"]
    )

    overtime = clean_overtime(
        data["overtime"]
    )

    production = clean_production(
        data["production"]
    )

    quality = clean_quality(
        data["quality"]
    )

    return {

        "employees": employees,

        "attendance": attendance,

        "overtime": overtime,

        "production": production,

        "quality": quality

    }
if __name__ == "__main__":

    from extract import extract_data

    data = extract_data()

    transformed = transform_data(data)

    for name, df in transformed.items():

        print(f"{name}: {df.shape}")
