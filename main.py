"""
To run the program and get the plots
"""

# Importing the necessary libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the functions from the src folder
from src.utils import mix_data, get_data, data_to_plot
from src.plots import make_plots

# Creating the main function

# inputs
# file1: r"Data\Agrofood_co2_emission.csv"
# file2: r"Data\gdp.csv"

def main(file1):
    # Making a data frame with the processed data path
    file_mix = pd.read_csv(file1)

    # Columns to plot
    columns_to_plot = ["Average Temperature °C", "total emission", "GDP"]

    # Making the plots
    make_plots(file_mix, columns_to_plot)

    # Showing the plots
    plt.show()

# Running the main function
if __name__ == "__main__":
    main("Data\processed_data.csv")