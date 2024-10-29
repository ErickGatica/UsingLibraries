"""
Script to make the plots of the data
"""
# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os 

from src.utils import data_to_plot

# Function to make the plots of the data 
# This function receives the data and the columns to plot
# we will generate a 4 - panel plot with the data for Mexico, Canada, and United States
# Top left (A): Line plot of Year vs Average Temperature. Only plot the data for Mexico, Canada, and the United States. 
# Lines should be colored according to the country and there should be a legend.
# Top right (B): Scatter plot of year vs total greenhouse gas emissions from various sources (there’s a column for this in the dataset). 
# Only plot the data for Mexico, Canada, and the United States–they should be colored to match the line plots in panel A and include a legend.
# Bottom left (C): Scatter plot of GDP (from gdp.csv) vs total emissions for those countries colored by year.
# Bottom right (D): Scatter plot of GDP vs average temperature colored by year.

# so we need the data: 
# Year
# Average Temperature °C
# total emission
# GDP
# Country


def make_plots(data, columns_to_plot):
    """
    This function plots the data for Mexico, Canada, and the United States in a 4-panel plot with the data for the columns specified

    Inputs:
    data: pandas dataframe with the data of Mexico, Canada, and the United States
    columns_to_plot: list of strings with the columns to plot

    Output:
    None
    """

    # Getting the data for Mexico, Canada, and the United States
    data_dict = data_to_plot(data)

    # Creating the figure
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    # Figure a Year vs Average Temperature
    for country in data_dict.keys():
        axs[0, 0].plot(data_dict[country]["Year"], data_dict[country][columns_to_plot[0]], label=country)
    axs[0, 0].set_xlabel("Year")
    axs[0, 0].set_ylabel(columns_to_plot[0])
    # Color palette
    sns.set_palette("husl")
    axs[0, 0].legend()
    # Add label A
    axs[0, 0].text(0.5, 1, 'A', transform=axs[0, 0].transAxes, fontsize=16, verticalalignment='top', horizontalalignment='center')
    # Removing top and right border of the plot
    axs[0, 0].spines['top'].set_visible(False)
    axs[0, 0].spines['right'].set_visible(False)

    # Figure b Year vs total emission
    for country in data_dict.keys():
        axs[0, 1].scatter(data_dict[country]["Year"], data_dict[country][columns_to_plot[1]], label=country , alpha=0.5)
    axs[0, 1].set_xlabel("Year")
    axs[0, 1].set_ylabel(columns_to_plot[1])
    # Color palette
    sns.set_palette("husl")
    axs[0, 1].legend()
    # Add label B
    axs[0, 1].text(0.5, 1, 'B', transform=axs[0, 1].transAxes, fontsize=16, verticalalignment='top', horizontalalignment='center')
    # Removing top and right border of the plot
    axs[0, 1].spines['top'].set_visible(False)
    axs[0, 1].spines['right'].set_visible(False)


    # Figure c GDP vs total emission
    for country in data_dict.keys():
        axs[1, 0].scatter(data_dict[country][columns_to_plot[2]], data_dict[country][columns_to_plot[1]], label=country , alpha=0.5)
    axs[1, 0].set_xlabel(columns_to_plot[2])
    axs[1, 0].set_ylabel(columns_to_plot[1])
    # Color palette
    sns.set_palette("husl")
    axs[1, 0].legend()
    # Add label C
    axs[1, 0].text(0.5, 1, 'C', transform=axs[1, 0].transAxes, fontsize=16, verticalalignment='top', horizontalalignment='center')
    # Removing top and right border of the plot
    axs[1, 0].spines['top'].set_visible(False)
    axs[1, 0].spines['right'].set_visible(False)


    # Figure d GDP vs Average Temperature °C
    for country in data_dict.keys():
        axs[1, 1].scatter(data_dict[country][columns_to_plot[2]], data_dict[country][columns_to_plot[0]], label=country , alpha=0.5)
    axs[1, 1].set_xlabel(columns_to_plot[2])
    axs[1, 1].set_ylabel(columns_to_plot[0])
    # Color palette
    sns.set_palette("husl")
    axs[1, 1].legend()
    # Add label D
    axs[1, 1].text(0.5, 1, 'D', transform=axs[1, 1].transAxes, fontsize=16, verticalalignment='top', horizontalalignment='center')
    # Removing top and right border of the plot
    axs[1, 1].spines['top'].set_visible(False)
    axs[1, 1].spines['right'].set_visible(False)

    # Saving the figure in folder figures
    if not os.path.exists("figures"):
        os.makedirs("figures")
    plt.savefig("figures/4_panel_plot.png")

    return None


