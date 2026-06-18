from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:500104@localhost:5432/company_db"
)

def load_to_postgres(data):

    data["employees"].to_sql(
        "employees",
        engine,
        if_exists="replace",
        index=False
    )

    print("employees loaded")

    data["attendance"].to_sql(
        "attendance",
        engine,
        if_exists="replace",
        index=False
    )

    print("attendance loaded")

    data["overtime"].to_sql(
        "overtime",
        engine,
        if_exists="replace",
        index=False
    )

    print("overtime loaded")

    data["production"].to_sql(
        "production",
        engine,
        if_exists="replace",
        index=False
    )

    print("production loaded")

    data["quality"].to_sql(
        "quality",
        engine,
        if_exists="replace",
        index=False
    )

    print("quality loaded")