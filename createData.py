import pandas as pd
import numpy as np
import random
import math

# Define constants
years = [2019, 2020, 2021, 2022, 2023]
num_trips_per_year = 20
num_employees = 100

# Generate Trip Information
trip_data = []
for year in years:
    for trip_id in range(1, num_trips_per_year + 1):
        length_of_trip = random.randint(2, 14)
        if length_of_trip >= 10:
            total_budget = round(random.uniform(4000, 5000), 2)
        elif length_of_trip <= 5:
            total_budget = round(random.uniform(2000, 3000), 2)
        else:
            total_budget = round(random.uniform(3000, 4000), 2)
        travel = round(random.uniform(0.3 * total_budget, 0.4 * total_budget), 2)
        lodging = round(random.uniform(0.3 * total_budget, 0.5 * total_budget), 2)
        dining = round(random.uniform(0.2 * total_budget, 0.3 * total_budget), 2)
        per_diem = round(random.uniform(0.1 * total_budget, 0.2 * total_budget), 2)
        incidental = round(random.uniform(0.1 * total_budget, 0.2 * total_budget), 2)
        total_budget = math.ceil(round((travel + lodging + dining + per_diem + incidental), -3))
        
        trip_data.append([trip_id, year, length_of_trip, total_budget, travel, dining, lodging, per_diem, incidental])

trip_df = pd.DataFrame(trip_data, columns=['Trip ID', 'Year', 'Length of Trip in Days', 'Total Budget', 'Travel', 'Dining', 'Lodging', 'Per Diem', 'Incidental'])

# Generate Expenditures
expenditure_data = []
expense_names = ["Delta Airlines", "Hilton Downtown", "The Cheesecake Factory", "Uber Ride", "Starbucks", "United Airlines", "Marriott",
                 "Olive Garden", "Lyft Ride", "American Airlines", "Grand Hotel", "Ruth\'s Chris Steak House", "Taxi Service", " Flat Tire", "Golf Trip",
                 "Cinema", "Burger King", "Housecleaning Fee", "Southwest Airlines", "Sheraton", "The Capital Grille", "JetBlue Airways", "Holiday Inn", 
                 "Panera Bread", "Parking Ticket", "MedCheck", "Driving Range", "Office Depot", "Bell-Hop Tip", "Dry Cleaning", "Car Rental", "Customer Appreciation Gift"
                 "Bottle Service", "Hotel Phone Bill", "Gas", "Dunkin\' Donuts", "McDonald\'s", "Wendy\'s", "Taco Bell", "Chick-fil-A", "Laundromat", "KFC", "St. Elmo\'s", 
                 "Bonefish Grill", "BJ\'s Brewhouse", "Spirit Airlines", "Outback Steakhouse", "Toll Fee"]

for year in years:
    for trip_id in range(1, num_trips_per_year + 1):
        if length_of_trip >= 10:
            num_expenses = random.randint(40, 50)
        elif length_of_trip <= 5:
            num_expenses = random.randint(10, 20)
        else:
            num_expenses = random.randint(20, 40)
        for charge_number in range(1, num_expenses + 1):
            employee_id = random.randint(1, num_employees)
            expense_name = random.choice(expense_names)
            if expense_name in ("Delta Airlines" , "Uber Ride" , "United Airlines" , "Lyft Ride" , "American Airlines" , "Taxi Service" , "Southwest Airlines" , "JetBlue Airways", "Car Rental", "Gas", "Spirit Airlines"):
                expense_category = 'Travel'
                if expense_name in ("Uber Ride", "Lyft Ride", "Taxi Service", "Gas"):
                    price = round(random.uniform(50.00, 200.00), 2)
                else:
                    price = round(random.uniform(100.00, 500.00), 2)
            elif expense_name in ("The Cheesecake Factory" , "Starbucks" , "Olive Garden" , "Ruth\'s Chris Steak House", "St. Elmo\'s", "Bonefish Grill", "BJ\'s Brewhouse",
                                  "Burger King", "The Capital Grille", "Panera Bread", "Dunkin\' Donuts", "McDonald\'s", "Wendy\'s", "Taco Bell", "Chick-fil-A", "KFC", "Outback Steakhouse"):
                expense_category = 'Dining'
                if expense_name in ("Starbucks", "Burger King", "Dunkin\' Donuts", "McDonald\'s", "Wendy\'s", "Taco Bell", "Chick-fil-A", "KFC"):
                    price = round(random.uniform(10.00, 80.00), 2)
                else:
                    price = round(random.uniform(100.00, 300.00), 2)
            elif expense_name in ("Hilton Downtown" , "Marriott" , "Grand Hotel" , "Sheraton" , "Holiday Inn"):
                expense_category = 'Lodging'
                price = round(random.uniform(300.00, 1000.00), 2)
            elif expense_name in ('Flat Tire' , "Housecleaning Fee" , "Parking Ticket" , "MedCheck", "Bell-Hop Tip", "Dry Cleaning", "Hotel Phone Bill", "Toll Fee"):
                expense_category = 'Incidental'
                price = round(random.uniform(10.00, 500.00), 2)
            else:
                expense_category = 'Other'
                price = round(random.uniform(10.00, 250.00), 2)
            
            expenditure_data.append([employee_id, trip_id, year, charge_number, expense_name, expense_category, price])

expenditure_df = pd.DataFrame(expenditure_data, columns=['Employee ID', 'Trip ID', 'Year', 'Charge Number', 'Expense Name', 'Expense Category', 'Price'])

# Save data to CSV files (optional)
trip_df.to_csv('trip_information.csv', index=False)
expenditure_df.to_csv('expenditures.csv', index=False)
