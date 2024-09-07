# Credit Card Expense Reporting Application

## Overview

The Credit Card Expense Reporting Application is designed to address the need for efficient budgeting and financial oversight by analyzing company credit card expenditures. It processes historical expense data, identifies spending trends, and provides predictive insights to improve future budget planning.

### Jupyter Notebook Link

- **MUST HAVE CSV FILES:** [Google Colab Notebook](https://colab.research.google.com/drive/1kcNTUj6hnwmr6QdchR1EncKv2fgENMsz?usp=sharing)

## Analysis

### Project Topic and Description

- **Project Topic:** Credit Card Expense Management
- **Description:** Analyzes credit card expense reports from 100 employees over 20 annual work trips spanning the last 5 fiscal years. Focuses on organizing and analyzing expenditure data to aid in budget formulation and detect trends and anomalies.

### Project Purpose and Goals

- **Purpose:** Enhance financial planning and management by analyzing company credit card expenditures.
- **Goals:**
  - Collect and systematically organize expense data.
  - Identify and analyze spending trends and anomalies.
  - Provide actionable insights for future budget planning and financial oversight.

### Descriptive Method

- **Charts and Graphs:** Visualizations of spending patterns, trends over time, and deviations from budget.
- **Tables:** Detailed tables showing average spending, total expenses by category, and individual trip expenditures.
- **Insights:** Highlight average spending, detect over-budget categories, and identify under-utilized funds.

### Predictive or Prescriptive Method

- **Graphs and Charts:** Visualize spending trends with best-fit lines to assist in future budget planning.
- **Forecasting:** Predict future budget-planning based on historical spending data.
- **Clustering Algorithm:** Apply DBSCAN clustering to categorize spending patterns and identify anomalies.

## Design and Development

### Computer Science Application Type

- **Type:** Web Application
- **Integration:** Designed for integration into a company’s financial system for use by accounting teams.

### Programming/Development Languages

- **Languages:** Python (Pandas, Numpy, Sklearn, Matplotlib)
- **Tools:** Jupyter Lab/Notebook, Google Colab
- **Database:** CSV Files
- **Version Control:** GitHub

### Operating Systems/Platforms

- **OS:** Windows 11 Home
- **IDE:** Visual Studio Code (Version 1.92)

## Implementation and Evaluation

### Execution Approach

1. **Data Import:** Import historical expense data from CSV files.
2. **Data Cleaning and Organization:** Clean and normalize data, addressing missing values and inconsistencies. Organize data for effective analysis.
3. **Data Analysis:**
   - **Descriptive Analysis:** Summarize spending data by category, trip, and employee.
   - **Predictive Analysis:** Implement DBSCAN clustering for spending patterns, and logistic regression for forecasting and anomaly detection.
4. **Visualization:** Develop charts and graphs for spending data, including bar charts, line graphs, and pie charts.
5. **User Interaction:** Develop an interactive interface for exploring data by trip, employee, category, and spending thresholds.
6. **Machine Learning Implementation:** Use DBSCAN for data categorization and anomaly detection, and logistic regression for trend forecasting.
7. **Dashboard Development:** Build a user-friendly dashboard with diverse visualizations for real-time data analysis and decision-making.

## Project Requirements Met

- **Descriptive Method:** Implemented current spending analysis and visualization.
- **Predictive Method:** Forecasting and trend analysis using machine learning algorithms.
- **Datasets:** Utilized historical credit card expense data.
- **Decision Support Functionality:** Provided tools for detailed financial analysis and budgeting.
- **Data Handling:** Featurizing, parsing, cleaning, and wrangling datasets.
- **Visualization:** Developed effective charts and graphs.
- **Interactive Queries:** Enabled dynamic querying and data views based on user input.
- **Machine Learning:** Applied clustering and regression methods for advanced analysis.
- **Accuracy Evaluation:** Techniques for evaluating the accuracy of predictions and analyses.
- **Security Features:** Ensured data protection with appropriate security measures.
- **Maintenance Tools:** Provided tools for ongoing monitoring and maintenance.
- **Dashboard:** Created a functional dashboard with multiple visualization types.

## Included Files

- **`createData.py`**: A script used to generate and simulate data for testing and development purposes.
- **`main.py`**: The main application file that runs the core functionality of the Credit Card Expense Reporting Application.
- **`expenditures.csv`**: A CSV file containing historical expenditure data used for analysis.
- **`trip_information.csv`**: A CSV file with trip budget information used to correlate with expenditure data.

## Skills Gleaned

- **Python Expertise:** Advanced proficiency with Pandas, Numpy, and Matplotlib.
- **Machine Learning Implementation:** Applied clustering and regression algorithms.
- **Data Handling:** Experience in cleaning, wrangling, and organizing data.
- **User Interface Development:** Developed interactive interfaces for real-time data analysis.
- **Data Visualization:** Created charts and graphs for visualizing spending patterns.
- **Version Control:** Managed project versions and changes using GitHub.
- **Project Management:** Organized and documented the project to meet requirements.
