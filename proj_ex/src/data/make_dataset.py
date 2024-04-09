import pandas as pd

def read_and_process_data(path):
    df = pd.read_parquet(path)
    df = df.dropna()
    return df