from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("🚀 Starting F1 Data Pipeline...")

    # Step 1: Extract
    raw_data = extract_data()

    # Step 2: Transform
    clean_data = transform_data(raw_data)

    # Step 3: Load
    load_data(clean_data)

    print("✅ Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()