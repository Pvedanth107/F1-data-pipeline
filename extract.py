import pandas as pd

def extract_data():
    print("📥 Extracting data...")

    drivers = pd.read_csv("data/drivers.csv")
    return drivers