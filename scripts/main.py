from extract import extract_data
from transform import transform_data
from load import load_to_postgres

def run_pipeline():

    print("Starting ETL Pipeline...")

    raw_data = extract_data()

    print("Extraction Complete")

    clean_data = transform_data(raw_data)

    print("Transformation Complete")

    load_to_postgres(clean_data)

    print("Loading Complete")

    print("Pipeline Finished Successfully")

if __name__ == "__main__":

    run_pipeline()