# Tyler Petrow
# ID: 011118169
# WGU C964 - Computer Science Capstone
# SIM3 Task 2: Capstone Project Design and Development
# Company Credit Card Expense Reporting and Forecasting Application

# import necessary libraries
import os
from tabulate import tabulate
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in CSV files "expenditures.csv" and "trip_information.csv"
expendituresDF = pd.read_csv('expenditures.csv')
budgetDF = pd.read_csv('trip_information.csv')

# separate each year total spending data
totalTripSpending2019 = pd.DataFrame(expendituresDF[expendituresDF['Year'] == 2019]).groupby(['Trip ID'])['Price'].sum()
totalTripSpending2020 = pd.DataFrame(expendituresDF[expendituresDF['Year'] == 2020]).groupby(['Trip ID'])['Price'].sum()
totalTripSpending2021 = pd.DataFrame(expendituresDF[expendituresDF['Year'] == 2021]).groupby(['Trip ID'])['Price'].sum()
totalTripSpending2022 = pd.DataFrame(expendituresDF[expendituresDF['Year'] == 2022]).groupby(['Trip ID'])['Price'].sum()
totalTripSpending2023 = pd.DataFrame(expendituresDF[expendituresDF['Year'] == 2023]).groupby(['Trip ID'])['Price'].sum()

# separate each year total budget data
totalBudget2019 = pd.DataFrame(budgetDF[budgetDF['Year'] == 2019]).groupby(['Trip ID'])['Total Budget'].sum()
totalBudget2020 = pd.DataFrame(budgetDF[budgetDF['Year'] == 2020]).groupby(['Trip ID'])['Total Budget'].sum()
totalBudget2021 = pd.DataFrame(budgetDF[budgetDF['Year'] == 2021]).groupby(['Trip ID'])['Total Budget'].sum()
totalBudget2022 = pd.DataFrame(budgetDF[budgetDF['Year'] == 2022]).groupby(['Trip ID'])['Total Budget'].sum()
totalBudget2023 = pd.DataFrame(budgetDF[budgetDF['Year'] == 2023]).groupby(['Trip ID'])['Total Budget'].sum()

# dataframes used for 5-year summary info
total5YearSpending = pd.DataFrame(expendituresDF).groupby(['Year','Trip ID'])['Price'].sum()
total5YearBudgets = pd.DataFrame(budgetDF).groupby(['Year','Trip ID'])['Total Budget'].sum()