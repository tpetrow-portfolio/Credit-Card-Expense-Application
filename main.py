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


# function will formulate trip report from user input year and trip number
def tripReport(userYear, userTrip):
  # convert user input to integer
  userYear = int(userYear)
  userTrip = int(userTrip)

  # separate expenditure data from year DF into each expenditure category for reporting
  travel = expendituresDF[(expendituresDF['Trip ID'] == userTrip) &    # filter expenditures for the user-selected trip and year, and 'Travel' category
                           (expendituresDF['Year'] == userYear) &
                           (expendituresDF['Expense Category'] == 'Travel')]
  lodging = expendituresDF[(expendituresDF['Trip ID'] == userTrip) &  # filter expenditures for the user-selected trip and year, and 'Lodging' category
                           (expendituresDF['Year'] == userYear) &
                           (expendituresDF['Expense Category'] == 'Lodging')]
  dining = expendituresDF[(expendituresDF['Trip ID'] == userTrip) &  # filter expenditures for the user-selected trip and year, and 'Dining' category
                           (expendituresDF['Year'] == userYear) &
                           (expendituresDF['Expense Category'] == 'Dining')]
  incidental = expendituresDF[(expendituresDF['Trip ID'] == userTrip) &  # filter expenditures for the user-selected trip and year, and 'Incidental' category
                           (expendituresDF['Year'] == userYear) &
                           (expendituresDF['Expense Category'] == 'Incidental')]
  per_diem = expendituresDF[(expendituresDF['Trip ID'] == userTrip) &  # filter expenditures for the user-selected trip and year, and 'Other' category
                           (expendituresDF['Year'] == userYear) &
                           (expendituresDF['Expense Category'] == 'Other')]


  # separate budget data from budget DF into each budget category for reporting
  travelBudget = budgetDF[(budgetDF['Trip ID'] == userTrip) &    # filter budget for the user-selected trip and year, and 'Travel' category
                          (budgetDF['Year'] == userYear)].iloc[0]['Travel']
  lodgingBudget = budgetDF[(budgetDF['Trip ID'] == userTrip) &    # filter budget for the user-selected trip and year, and 'Lodging' category
                           (budgetDF['Year'] == userYear)].iloc[0]['Lodging']
  diningBudget = budgetDF[(budgetDF['Trip ID'] == userTrip) &    # filter budget for the user-selected trip and year, and 'Dining' category
                          (budgetDF['Year'] == userYear)].iloc[0]['Dining']
  incidentalBudget = budgetDF[(budgetDF['Trip ID'] == userTrip) &    # filter budget the for user-selected trip and year, and 'Incidental' category
                              (budgetDF['Year'] == userYear)].iloc[0]['Incidental']
  per_diemBudget = budgetDF[(budgetDF['Trip ID'] == userTrip) &    # filter budget for the user-selected trip and year, and 'Other' category
                            (budgetDF['Year'] == userYear)].iloc[0]['Per Diem']
  totalBudget = budgetDF[(budgetDF['Trip ID'] == userTrip) &    # filter budget for the user-selected trip and year, and 'Total' column
                         (budgetDF['Year'] == userYear)].iloc[0]['Total Budget']

  
  # create subplots
  fig, axes = plt.subplots(nrows=6, ncols=2, figsize=(20, 40))
  fig.subplots_adjust(left= 0.125, bottom=0.03, right=0.7, top=0.95, hspace=1, wspace=0.25)  # adjust top margin and vertical spacin
    
  # function to create pie charts
  def plot_pie(ax, spent, budget, title):
        spent_percentage = (spent / budget) * 100
        remaining_percentage = 100 - spent_percentage
        if remaining_percentage < 0:
            remaining_percentage = 0
        data = np.array([spent_percentage, remaining_percentage])
        ax.pie(data, autopct='%1.1f%%',
               explode=[0.1, 0], colors=['red', 'green'], shadow=True)
        ax.set_title(title)
        ax.axis('equal')
    
  # function to create bar charts
  def plot_bar(ax, spent, budget, title):
        remaining = budget - spent
        ax.bar(['Budgeted', 'Spent', 'Remaining'], [budget, spent, remaining],
               color=['black', 'red', 'green'])
        for bar in ax.patches:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}',
                    ha='center', va='bottom')
        ax.set_title(title)
        ax.set_ylabel('Amount ($)')
    
  # plot Travel
  plot_pie(axes[0, 0], travel['Price'].sum(), travelBudget, 'Travel Pie')
  plot_bar(axes[0, 1], travel['Price'].sum(), travelBudget, 'Travel Bar')

  # plot Lodging
  plot_pie(axes[1, 0], lodging['Price'].sum(), lodgingBudget, 'Lodging Pie')
  plot_bar(axes[1, 1], lodging['Price'].sum(), lodgingBudget, 'Lodging Bar')

  # plot Dining
  plot_pie(axes[2, 0], dining['Price'].sum(), diningBudget, 'Dining Pie')
  plot_bar(axes[2, 1], dining['Price'].sum(), diningBudget, 'Dining Bar')

  # plot Incidental
  plot_pie(axes[3, 0], incidental['Price'].sum(), incidentalBudget, 'Incidental Pie')
  plot_bar(axes[3, 1], incidental['Price'].sum(), incidentalBudget, 'Incidental Bar')

  # plot Per Diem
  plot_pie(axes[4, 0], per_diem['Price'].sum(), per_diemBudget, 'Per Diem Pie')
  plot_bar(axes[4, 1], per_diem['Price'].sum(), per_diemBudget, 'Per Diem Bar')

  # plot Total Budget
  totalSpentPerc = ((travel['Price'].sum() + lodging['Price'].sum() +
                 dining['Price'].sum() + incidental['Price'].sum() +
                 per_diem['Price'].sum()) / totalBudget) * 100
  totalRemaining = 100 - totalSpentPerc
  if totalRemaining < 0:  # if remaining percentage in budget is less than 0, make it 0
      totalRemaining = 0
  total_data = np.array([totalSpentPerc, totalRemaining])
  axes[5, 0].pie(total_data, autopct='%1.1f%%',
                 explode=[0.1, 0], colors=['red', 'green'], shadow=True)
  axes[5, 0].set_title('Total Expenditure Pie')
  axes[5, 0].axis('equal')
  
  totalSpentAmount = travel['Price'].sum() + lodging['Price'].sum() + dining['Price'].sum() + incidental['Price'].sum() + per_diem['Price'].sum()
  plot_bar(axes[5, 1], totalSpentAmount, totalBudget, 'Total Expenditure Bar')
  
  plt.show()  # display the entire figure

# tripReport(2019,2)  # test function