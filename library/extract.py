# Extract csv file from url link
import pandas as pd

def extract_file():
    data = pd.read_csv("Data/subset.csv")
    return data