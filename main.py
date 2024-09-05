# Tyler Petrow
# ID: 011118169
# WGU C964 - Computer Science Capstone
# SIM3 Task 2: Capstone Project Design and Development
# Company Credit Card Expense Reporting and Forecasting Application

# import necessary libraries
import os
from tabulate import tabulate
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in CSV files "expenditures.csv" and "trip_information.csv"
expendituresDF = pd.read_csv('expenditures.csv')
budgetDF = pd.read_csv('trip_information.csv')

# aggregate total ependitures for later use
total_expenditures = expendituresDF.groupby(['Trip ID', 'Year'])['Price'].sum().reset_index()
total_expenditures.columns = ['Trip ID', 'Year', 'Total Expenditure']

# merge total budget per trip with total spending per trip
merged_DF = pd.merge(budgetDF, total_expenditures, on=['Trip ID', 'Year'])


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
  fig.subplots_adjust(left= 0.125, bottom=0.03, right=0.7, top=0.95, hspace=1, wspace=0.25)  # adjust top margin and vertical spacing
    
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

  plt.tight_layout()
  
  plt.show()  # display the entire figure


# function will formulate tabulated table of charges from user input year, and trip
def chargeTable_by_trip(userYear, userTrip):
  # convert user input to integer
  userYear = int(userYear)
  userTrip = int(userTrip)

  # filter expenditures for the user-selected trip and year
  all_trip_charges = expendituresDF[(expendituresDF['Trip ID'] == userTrip) &    
                    (expendituresDF['Year'] == userYear)].sort_values(by = 'Expense Category')
  
  # drop the index column, not needed in table
  all_trip_charges = all_trip_charges.reset_index(drop=True)  

  # create list of column headers for table
  headerList = ['Employee ID','Trip ID','Trip Year','Charge Number', 'Expense Name', 'Expense Category', "Price"]

  # create table of charges from user-selected trip and year
  chargeTable = tabulate(all_trip_charges, headers=headerList, tablefmt='fancy_grid', showindex=False)
  
  print(chargeTable)  # print table


# function will formulate tabulated table of charges from user input year
def chargeTable_by_year(userYear):
  # convert user input to integer
  userYear = int(userYear)

  # total expenditure data filtered out from expendituresDF
  year_expenditure_data = pd.DataFrame(expendituresDF[expendituresDF['Year'] == userYear])  

  # create list of column headers for table
  headerList = ['Employee ID','Trip ID','Trip Year','Charge Number', 'Expense Name', 'Expense Category', "Price"]  

  # create table of charges from user-selected trip and year
  chargeTable = tabulate(year_expenditure_data, headers=headerList, tablefmt='fancy_grid', showindex=False)  

  print(chargeTable)  # print table


# function will formulate tabulated table of over-budget trips
def over_budget_table():
  # filter trips where expenditures exceed the budget
  overBudget = merged_DF[merged_DF['Total Expenditure'] > merged_DF['Total Budget']]
  
  # sort by Total Expenditure in descending order
  overBudget = overBudget.sort_values(by='Total Expenditure', ascending=False)
  
  # reset index for better table formatting
  overBudget = overBudget.reset_index(drop=True)
  
  # select relevant columns for the table
  overBudgetTable = overBudget[['Trip ID', 'Year', 'Total Expenditure']]
  
  # create list of column headers for the table
  headerList = ['Trip ID', 'Year', 'Total Expenditure']
  
  # create table using tabulate
  chargeTable = tabulate(overBudgetTable, headers=headerList, tablefmt='fancy_grid', showindex=False)
  
  # print the table
  print(chargeTable)


# function will formulate summary report from user input year, and has ability to create a subplot if needed
def yearReport(userYear, userax=None):
  # note: userax helps when calling yearReport with only one parameter (i.e. yearReport(2019))

  # convert user input to integer
  userYear = int(userYear)
    
  # parse dataframes for user-specified data
  year_expenditure_data = pd.DataFrame(expendituresDF[expendituresDF['Year'] == userYear])
  year_budget_data = pd.DataFrame(budgetDF[budgetDF['Year'] == userYear])
  totalYearSpending = year_expenditure_data.groupby('Trip ID')['Price'].sum()
  totalYearBudget = year_budget_data.groupby('Trip ID')['Total Budget'].sum()
    
  # ensure both series have the same trip IDs for merging
  merged_data = pd.merge(totalYearSpending, totalYearBudget, left_index=True, right_index=True)
  merged_data.columns = ['Total Spending', 'Total Budget']
    
  # use provided Axes object or create a new one
  if userax is None:  # if the user does not specify an ax
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(left= 0.125, bottom=0.03, right=0.7, top=0.95, hspace=1, wspace=0.25)  # adjust top margin and vertical spacing
  else:  # if the user specifies an ax
     ax = userax
    
  # plot on the Axes object
  ax.scatter(merged_data.index, merged_data['Total Budget'], color='black', label='Budget', zorder=2, s=50)
  
  colors = ['red' if spending > budget else 'green' for spending, budget in zip(merged_data['Total Spending'], merged_data['Total Budget'])]
  sizes = [100 if color == 'red' else 50 for color in colors]
  ax.scatter(merged_data.index, merged_data['Total Spending'], color=colors, edgecolor='black', label='Spending', zorder=3, s=sizes)

  ax.set_xticks(range(1, 21))  # put all 20 trips on x-axis

  # add labels and title
  ax.set_xlabel('Trip Number')
  ax.set_ylabel('Dollar Amount')
  ax.set_title('Trip Spending and Budget Comparison for ' + str(userYear))

  ax.grid(True)  # add grid for readability

  if userax is None:
    plt.show()  # display the plot if no Axes object was passed


# function will cluster data utilizing DBSCAN algorithm, finding relationship between expenditure amounts vs total length of trip
def trip_clustering():
  # prepare features for clustering
  features = merged_DF[['Total Expenditure', 'Length of Trip in Days']]

  # normalize features
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(features)

  # apply DBSCAN
  dbscan_model = DBSCAN(eps=0.5, min_samples=5)
  dbscan_result = dbscan_model.fit_predict(X_scaled)

  # add clustering results to DataFrame
  merged_DF['Cluster'] = dbscan_result

  # plot DBSCAN clusters
  plt.figure(figsize=(12, 6))

  # plot each cluster
  unique_clusters = np.unique(dbscan_result)
  for cluster in unique_clusters:
      cluster_data = merged_DF[merged_DF['Cluster'] == cluster]
      plt.scatter(cluster_data['Total Expenditure'], cluster_data['Length of Trip in Days'], 
                  label=f'Cluster {cluster}' if cluster != -1 else 'Noise', 
                  alpha=0.6, edgecolors='w')

  # highlight noise points (outliers)
  noise = merged_DF[merged_DF['Cluster'] == -1]
  plt.scatter(noise['Total Expenditure'], noise['Length of Trip in Days'], color='black', label='Noise', marker='x')

  plt.xlabel('Total Expenditure')
  plt.ylabel('Total Length of Trip')
  plt.title('DBSCAN Clustering of Expenditure vs. Trip Length')
  plt.legend()
  plt.show()


# function will generate a subplot of 5 years of data using yearReport function
def five_year_report():  
  years = budgetDF['Year'].unique()  # define years for the subplots - allows for scalability in future

  fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(5, 10))  # create a 3x2 grid of subplots
  axes = axes.flatten()  # flatten the 2D array of axes for easy iteration
  
  # generate plots for each year
  for i, year in enumerate(years):
      yearReport(year, axes[i])
    
  axes[len(years)].axis('off')  # hide the unused subplot

  plt.subplots_adjust(left=0.04, right=1, top=0.95, bottom=0.1, wspace=0.223, hspace=0.45)
    
  plt.tight_layout()
  plt.show()


# function will generate a pie chart of the percentage of trips that are over/under budget
def average_pie():

  # Identify trips where expenditures exceed the budget
  overBudget = merged_DF[merged_DF['Total Expenditure'] > merged_DF['Total Budget']]

  # Calculate the total number of trips dynamically
  #total_trips = len(merged_DF)

  # calculate the percentage of over-budget trips
  over_percentage = len(overBudget)

  # create numpy array of over percentage and remaining percentage
  data = np.array([over_percentage, ((len(merged_DF))-over_percentage)])

  plt.pie(data, autopct='%1.1f%%', labels=['Over-Budget','Under-Budget'], explode=[0.1, 0], colors=['red', 'green'], shadow=True)
  plt.title('Over-Budget Average')
  plt.axis('equal')

  plt.tight_layout()

  plt.show()  # display the entire figure


# function will generate a bar chart of the top 10% most expensive trips, and highlight the most expensive trip's bar
def plot_most_expensive_trips():
    # identify the top 10% most expensive trips
    top_10_percent_threshold = merged_DF['Total Expenditure'].quantile(0.9)
    top_10_percent = merged_DF[merged_DF['Total Expenditure'] >= top_10_percent_threshold]

    # combine 'Trip ID' and 'Year' for x-axis labels
    x_labels = [f"Trip {tid}\nYear {yr}" for tid, yr in zip(top_10_percent['Trip ID'], top_10_percent['Year'])]

    plt.figure(figsize=(14, 7))
    bars = plt.bar(x_labels, top_10_percent['Total Expenditure'], color='skyblue')
    plt.xlabel('Trip ID and Year')
    plt.ylabel('Total Expenditure')
    plt.title('Top 10% Most Expensive Trips')

    # highlight the most expensive trip
    max_expense_index = top_10_percent['Total Expenditure'].idxmax()
    bars[top_10_percent.index.get_loc(max_expense_index)].set_color('red')

    plt.tight_layout()

    plt.xticks(rotation=90)
    plt.show()


# function will generate a bar chart of the bottom 10% least expensive trips, and highlight the least expensive trip's bar
def plot_cheapest_trips():
    # identify the bottom 10% least expensive trips
    bottom_10_percent_threshold = merged_DF['Total Expenditure'].quantile(0.1)
    bottom_10_percent = merged_DF[merged_DF['Total Expenditure'] <= bottom_10_percent_threshold]

    # combine 'Trip ID' and 'Year' for x-axis labels
    x_labels = [f"Trip {tid}\nYear {yr}" for tid, yr in zip(bottom_10_percent['Trip ID'], bottom_10_percent['Year'])]

    plt.figure(figsize=(14, 7))
    bars = plt.bar(x_labels, bottom_10_percent['Total Expenditure'], color='lightgreen')
    plt.xlabel('Trip ID and Year')
    plt.ylabel('Total Expenditure')
    plt.title('Bottom 10% Least Expensive Trips')

    # highlight the least expensive trip
    min_expense_index = bottom_10_percent['Total Expenditure'].idxmin()
    bars[bottom_10_percent.index.get_loc(min_expense_index)].set_color('orange')

    plt.tight_layout()

    plt.xticks(rotation=90)
    plt.show()


# function will generate a new budget amount for each budget category from past 5 year expenditure data
def forecast():
  # list of years to plot
  years = budgetDF['Year'].unique()  # define years for the subplots - allows for scalability in future
  
  # prepare a DataFrame to hold average expenditures for each year
  avg_expenditure = pd.DataFrame()
  
  # calculate the average expenditure for each category by year
  for year in years:
    year_data = expendituresDF[expendituresDF['Year'] == year]
    avg_per_category = year_data.groupby('Expense Category')['Price'].mean().reset_index()
    avg_per_category['Year'] = year
    avg_expenditure = pd.concat([avg_expenditure, avg_per_category], axis=0)
  
  # calculate the overall mean expenditure for each category
  overall_avg = expendituresDF.groupby('Expense Category')['Price'].mean().reset_index()
  overall_avg['Year'] = 'Mean'
  
  # plot the data
  plt.figure(figsize=(14, 8))
  colors = ['blue', 'orange', 'green', 'red', 'purple']
  
  for i, year in enumerate(years):
    year_data = avg_expenditure[avg_expenditure['Year'] == year]
    plt.plot(year_data['Expense Category'], year_data['Price'], 
              linestyle='--', marker='o', markersize=2, color=colors[i], 
              alpha=0.5, label=f'{year}')
  
  # plot the mean line
  plt.plot(overall_avg['Expense Category'], overall_avg['Price'], 
            linestyle='-', marker='o', color='black', 
            linewidth=2.5, markersize=8, label='Forecasted Budget')
  
  plt.xlabel('Category')
  plt.ylabel('Average Expenditure')
  plt.title('Average Expenditure by Category for Each Year')
  plt.xticks(rotation=45, ha='right')
  plt.grid(True)
  plt.legend()
  plt.tight_layout()
  
  plt.show()


      # give user an option to see a table (would be one row)
        # Year                Category name -------  Total Budget
        # Forecasted (2024)     $$$ -----------------  $$$

      # because 75% of trips were under budget, the new budget might be lower than other budgets and can save company money



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
    print("3) Clustered Data")
    print("4) Forecast Data")
    print("5) About the Application")
    print("0) Exit")
    print("=================================")
    print("")
    mainSelect = input("Enter Selection: ")

    # if user selects a year to generate reports on
    if mainSelect in ['2019','2020','2021','2022','2023']:
      innerSelect = 1
      while innerSelect != 0:
        os.system('cls')
        print(mainSelect + " Year Reporting")
        print("---------------------------")
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
      five_year_report()
      innerSelect = 1
      while innerSelect != 0:
        os.system('cls')
        print("5-Year Summary Reporting")
        print("------------------------")
        print("1) Explore Total Over-Budget Trip Data")
        print("2) Explore Most Expensive Trip Data")
        print("3) Explore Least Expensive Trip Data")
        print("")
        print("Enter 0 to return to main menu")
        print("=================================")
        print("")
        innerSelect = input("Enter Selection: ")

        if innerSelect == "1":  # if user wants to explore total over-budget trip data
          average_pie()
          chargeTableDisplay = input("Would you like to see a list of all over-budget trips? (Y/N): ")
          if chargeTableDisplay in ('Y','y'):
              os.system('cls')
              over_budget_table()  # call over_budget_table function to print a chart of all over-budget trips
              print("")
              input("Press ENTER to return to main menu....")
              break
        elif innerSelect == "2":
          plot_most_expensive_trips()
        elif innerSelect == "3":
          plot_cheapest_trips()
        elif innerSelect == "0":
          break
        else:
            print("Invalid Selection")
            print(" ")   

    # if user selects 3) Clustered Data
    elif mainSelect == "3":
      trip_clustering()  # call trip_clustering function to display plot of clustered data
      os.system('cls')

    # if user selects 4) Forecast Data
    elif mainSelect == "4":
      forecast()  # call forecast function to display forecast line plot
      forecasted_budget_table()  # call forecasted_budget_table function to print table of new budget data
      os.system('cls')

    # if user selects 4) About the Application
    elif mainSelect == "5":
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
      print("GitHub Repository: https://github.com/tpetrow-portfolio/Credit-Card-Expense-Application/")
      print("")
      print("")
      input("Press ENTER to return to main menu....")

    # if user selects 0) Exit
    elif(mainSelect == "0"):
      os.system('cls')
      print("Exiting Application...")

    # if user makes incorrect selection
    else:
      os.system('cls')
      print("Invalid Selection...")

main()