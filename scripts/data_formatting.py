import pandas as pd
def format_data(data):
    """Formats the data for final analysis."""
    print("Formatting data...")

    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
        print("Data formatting completed.")
        return data