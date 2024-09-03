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


# function will formulate summary report from user input year
def chargeTable_by_trip(userYear, userTrip):
  # convert user input to integer
  userYear = int(userYear)
  userTrip = int(userTrip)

  all_trip_charges = expendituresDF[(expendituresDF['Trip ID'] == userTrip) &    # filter expenditures for the user-selected trip and year
                    (expendituresDF['Year'] == userYear)].sort_values(by = 'Expense Category')
  all_trip_charges = all_trip_charges.reset_index(drop=True)  # drop the index column, not needed in table
  headerList = ['Employee ID','Trip ID','Trip Year','Charge Number', 'Expense Name', 'Expense Category', "Price"]  # create list of column headers for table
  employeeTable = tabulate(all_trip_charges, headers=headerList, tablefmt='fancy_grid', showindex=False)  # create table of charges from user-selected trip and year
  
  print(employeeTable)  # print table


def chargeTable_by_year(userYear):
  # convert user input to integer
  userYear = int(userYear)

  year_expenditure_data = pd.DataFrame(expendituresDF[expendituresDF['Year'] == userYear])  # total expenditure data filtered out from expendituresDF
  headerList = ['Employee ID','Trip ID','Trip Year','Charge Number', 'Expense Name', 'Expense Category', "Price"]  # create list of column headers for table
  employeeTable = tabulate(year_expenditure_data, headers=headerList, tablefmt='fancy_grid', showindex=False)  # create table of charges from user-selected trip and year
  
  print(employeeTable)  # print table

###################################
# Main Menu UI of program
def main():
  mainSelect = "1"
  while mainSelect != "0":
    os.system('cls')  # clear screen
    print("Sample Co.'s Company Credit Card Expenditure Reporting and Forecasting Application")
    print("----------------------------------------------------------------------------------")
    print("1) Enter Year Number (2019-2023)")
    print("2) 5-year Summary Reporting")
    print("3) Forecast Data")
    print("4) About the Application")
    print("0) Exit")
    print("=================================")
    print("")
    mainSelect = input("Enter Selection: ")

    # if user selects a year to generate reports on
    if mainSelect in ['2019','2020','2021','2022','2023']:
      innerSelect = 1
      while innerSelect != 0:
        os.system('cls')
        print("Sample Co.'s Company Credit Card Expenditure Reporting and Forecasting Application")
        print("----------------------------------------------------------------------------------")
        print("Enter Trip Number (1-20)")
        print("  -OR-")
        print("Enter (s) for a summary of " + mainSelect)
        print("  -OR-")
        print("Enter 0 to return to main menu")
        print("=================================")
        print("")
        innerSelect = input("Enter Selection: ")
        if innerSelect in ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'):  # if user selects trip number 1-20
          tripReport(mainSelect, innerSelect)  # call tripReport function to generate charts for user-selected trip from user-selected year
          print("")
          chargeTableDisplay = input("Would you like to see a breakdown of all charges for trip # " + innerSelect + "? (Y/N): ")
          if chargeTableDisplay in ('Y','y'):
            os.system('cls')
            chargeTable_by_trip(mainSelect,innerSelect)  # call chargeTable_by_trip function to print a chart of all charges for the user-selected trip from user-selected year, organized by expense category
            print("")
            input("Press ENTER to return to main menu....")
            break
        elif innerSelect in ('s','S'):  # if user selects 's' for summary
          os.system('cls')
          yearReport(mainSelect)  # call yearReport function to generate summary charts for user-selected year
          chargeTableDisplay = input("Would you like to see a breakdown of all charges for " + mainSelect + "? (Y/N): ")
          if chargeTableDisplay in ('Y','y'):
            os.system('cls')
            chargeTable_by_year(mainSelect)  # call chargeTable_by_year function to print a chart of all charges from user-selected year, organized by trip number
            print("")
            input("Press ENTER to return to main menu....")
            break
        elif innerSelect == "0":  # if user selects 0 to return to main menu
          break
        else:
          print("Invalid Selection")
          print(" ")

    # if user selects 2) 5-year Summary Reporting
    elif mainSelect == "2":
      print("5-year Summary Reporting")

    # if user selects 3) Forecast Data
    elif mainSelect == "3":
      print("Forecast Data")

    # if user selects 4) About the Application
    elif mainSelect == "4":
      os.system('cls')
      print("About the Application")
      print("==========================")
      print("")
      print("Application Info:")
      print("==========================")
      print("Company Credit Card Reporting and Forecasting Application")
      print("WGU C964 - Computer Science Capstone")
      print("Version: 1.1")
      print("Release Notes: Final Submission for WGU Computer Science Capstone (SIM3 Task 2)")
      print("")
      print("Devloper Credits:")
      print("==========================")
      print("Author: Tyler Petrow")
      print("WGU Student ID: 011118169")
      print("GitHub Repository: https://github.com/tpetrow-portfolio")
      print("")
      break

    # if user selects 0) Exit
    elif(mainSelect == "0"):
      os.system('cls')
      print("Exiting Application...")

    # if user makes incorrect selection
    else:
      os.system('cls')
      print("Invalid Selection...")
      break

main()