# Tyler Petrow
# ID: 011118169
# WGU C964 - Computer Science Capstone
# SIM3 Task 2: Capstone Project Design and Development
# Company Credit Card Expense Reporting and Forecasting Application

# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in CSV files "expenditures.csv" and "trip_information.csv"
expendituresDF = pd.read_csv('expenditures.csv')
tripDF = pd.read_csv('trip_information.csv')

# test that each csv was read correctly
# print(expendituresDF.head())
# print()
# print(tripDF.head())

# separate expenditure data into each expenditure category
travel = pd.DataFrame(expendituresDF.loc[expendituresDF['Expense Category'] == 'Travel'])
lodging = pd.DataFrame(expendituresDF.loc[expendituresDF['Expense Category'] == 'Lodging'])
dining = pd.DataFrame(expendituresDF.loc[expendituresDF['Expense Category'] == 'Dining'])
incidental = pd.DataFrame(expendituresDF.loc[expendituresDF['Expense Category'] == 'Incidental'])
per_diem = pd.DataFrame(expendituresDF.loc[expendituresDF['Expense Category'] == 'Other'])

# function to organize expenditureDF based on user input year
def reportYear(userYear):
    returnYear = pd.DataFrame(expendituresDF.loc[expendituresDF['Year'] == userYear])
    return returnYear



    # MAIN MENU OF PROGRAM
    # Select an Option:
        # SECTION A
            #   1. 2019 Reporting
            #   2. 2020 Reporting
            #   3. 2021 Reporting
            #   4. 2022 Reporting
            #   5. 2023 Reporting
        # SECTION B
            #   6. 5-year Summary Reporting
        # SECTION C
            #   7. Forecast Data
        # SECTION D
            #   8. About the Application
    #   0. Exit