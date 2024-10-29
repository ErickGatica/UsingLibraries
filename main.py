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

# Files to read
file_agro = r"Data\Agrofood_co2_emission.csv"
file_gdp = r"Data\gdp.csv"

# Merging the data

data = mix_data(file_agro, file_gdp)

# Columns to plot
columns_to_plot = ["Average Temperature °C", "total emission", "GDP"]

# Making the plots
make_plots(data, columns_to_plot)

# Showing the plots
plt.show()


