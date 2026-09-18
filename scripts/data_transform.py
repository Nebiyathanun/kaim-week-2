import numpy as np
def transform_data(data):
    """Transforms the data by creating new features."""
    print("Transforming data...")

    data["Daily_Return"] = data["Close"].diff()

    data["MA_20"] = data["Close"].rolling(window=20).mean()
    print("Data transformation completed.")
    return data