import pandas as pd
from src.utils import mix_data

 # Read the input files
agrofood = "Data\Agrofood_co2_emission.csv"
gdp = "Data\gdp.csv"

# Creating function to process the data

def process_data(agrofood, gdp):
    """
    This function processes the data from the agrofood and gdp files

    Inputs:
    agrofood: str, path to the agrofood file
    gdp: str, path to the gdp file

    Output:
    merged_data: pandas dataframe with the merged data
    """
    # Process and clean the data
    merged_data = mix_data(agrofood, gdp)
    # Save the processed data
    merged_data.to_csv("Data/processed_data.csv", index=False)

    return merged_data