def transform_data(df):
    print("🔄 Transforming data...")

    df = df.dropna()   # remove missing values
    return df