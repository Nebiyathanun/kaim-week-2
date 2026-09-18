import pandas as pd
def read_csv(file_path):
    """Reads data from a CSV file."""
    print("Extracting data from CSV...")
    try:
        data = pd.read_csv(file_path)
        print("Data extraction successfu.")
        return data
        
    except Exception as e:
        print(f"Error during data extraction: {e}")
        return None
    

