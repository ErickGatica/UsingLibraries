import pandas as pd
from src.utils import mix_data
import os

 # Read the input files
agrofood = r"Data\Agrofood_co2_emission.csv"
gdp = r"Data\gdp.csv"

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


    # Ensure the Data directory exists
    output_dir = "Data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the processed data
    merged_data.to_csv(os.path.join(output_dir, "processed_data.csv"), index=False)

    # Checking if the data is saved correctly
    if os.path.exists(os.path.join(output_dir, "processed_data.csv")):
        print("Data saved successfully.")
    else:
        print("Error saving data.")


    return merged_data