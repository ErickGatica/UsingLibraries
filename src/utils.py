"""
This is the script with functions to extract the data and do operations
"""

#Importin libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Dictionary with the columns of the data from Agrofood_co2_emissions.csv
columns_to_ind = {
    "Area" : 0, #Country
    "Year" : 1,
    "Savanna fires" : 2,
    "Forest fires" : 3,
    "Crop Residues" : 4,
    "Rice Cultivation" : 5,
    "Drained organic soils" : 6,
    "Pesticides Manufacturing" : 7,
    "Food Transport" : 8,
    "Forestland" : 9,
    "Net Forest_conversion" : 10,
    "Food Household_Consumption" : 11,
    "Food Retail" : 12,
    "On farm_Electricity Use" : 13,
    "Food Packaging" : 14,
    "Agrifood Systems Waste Disposal" : 15,
    "Food Processing" : 16,
    "Fertilizers Manufacturing" : 17,
    "IPPU" : 18,
    "Manure applied to Soils" : 19,
    "Manure left on Pasture" : 20,
    "Manure Management" : 21,
    "Fires in organic soils" : 22,
    "Fires in humid tropical forests" : 23,
    "On farm energy use" : 24,
    "Rural population" : 25,
    "Urban population" : 26,
    "Total Population Male": 27,
    "Total Population Female": 28,
    "total emission" : 29,
    "Average Temperature" : 30
}


# Function to change the name of a country in the data because one file is United States of America and the other one United States

def change_country_name(data, old_name, new_name):
    """
    This function changes the name of a country in the data

    Inputs:
    data: pandas dataframe
    old_name: str, name of the country to change
    new_name: str, new name of the country

    Output:
    data: pandas dataframe with the name of the country changed
    """
    data["Country"] = data["Country"].replace(old_name, new_name)
    
    return data


# Function to mix the data from two different csv files and return a pandas dataframe
def mix_data(file1, file2):
    """
    This function mixes the data from two different csv files and returns a pandas dataframe

    Inputs:
    file1: str, name of the first csv file
    file2: str, name of the second csv file

    Output:
    data: pandas dataframe with the data from the two csv files merged
    """
    # Reading the data from the csv files
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    
    
    # Changing the name of the column United States of America to United States in the agrofood data
    data1["Country"] = data1["Country"].replace("United States of America", "United States")

    # Merging the data
    data = pd.merge(data1, data2, on = ["Country", "Year"])
    
    return data


# Function to get data from a specific country and column

def get_data(data, country, column):
    """
    This function returns the data from a specific country and column

    Inputs:
    data: pandas dataframe
    country: str, name of the country
    column: str, name of the column

    Output:
    data_column: pandas series with the data from the specific country and column
    """
    # Getting the index of the column
    ind = columns_to_ind[column]
    
    # Getting the data
    data_country = data[data["Country"] == country]
    data_column = data_country.iloc[:, ind]
    
    return data_column

# Function to create a dictionary with the data to make the 4-panel plot of the data

def data_to_plot(data):
    """
    This funtion creates a dictionary with the data to make the 4-panel plot of the data

    Inputs:
    data: pandas dataframe

    Output:
    data_dict: dictionary with the data for Mexico, Canada, and the United States
    """
    # Dictionary to store the data
    data_dict = {}
    
    # Getting the data for Mexico, Canada, and the United States
    data_dict["Mexico"] = data[data["Country"] == "Mexico"]
    data_dict["Canada"] = data[data["Country"] == "Canada"]
    data_dict["United States"] = data[data["Country"] == "United States"]
    
    return data_dict


"""

# Testing considering the files in the Data folder which is Data folde is in the same than src folder

file1 = "src\Agrofood_co2_emission.csv"
file2 = "src\gdp.csv"
data = mix_data(file1, file2)

# Getting the data from a specific country and column
country = "Argentina"
column = "Savanna fires"
data_column = get_data(data, country, column)
print(data_column)

"""


