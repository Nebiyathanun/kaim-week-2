import pandas as pd
import numpy as np

def clean_data(data):
     """Cleans the extracted data."""
     print("Cleaning data...")

     data = data.drop_duplicates()

     numeric_columns = ["Close", "High", "Low", "Open", "Volume"]
     for column in numeric_columns:
          data[column] = pd.to_numeric(data[column], errors="coerce")

          data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())
          print("Data cleaning completed.")
          return data

def clean_data_2(data):
     data.fillna(data.mean(numeric_only=True), inplace=True)

def treat_outliers_iqr(column):
     Q1 = column.quantile(0.25)
     Q3 = column.quantile(0.75)
     IQR = Q3 - Q1
     lower_bound = Q1 - 1.5 * IQR
     upper_bound = Q3 + 1.5 * IQR


     column_mean = column.mean()
     column = np.where((column < lower_bound) | (column > upper_bound), column_mean, column)
     return column