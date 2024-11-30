# Applying custom functions across rows/columns.

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Tom', 'Lucy'],
    'Age': [28, 34, 29, 31],
    'Salary': [50000, 60000, 55000, 70000]
}

df = pd.DataFrame(data)

# ---------------------------------------------------

# Define a custom function to add a bonus to the salary
def add_bonus(salary):
    return salary + 5000

# Apply the custom function to the 'Salary' column
df['Salary_with_Bonus'] = df['Salary'].apply(add_bonus)

print("DataFrame with Salary Bonus:")
print(df)
# Output:
# DataFrame with Salary Bonus:
#    Name  Age  Salary  Salary_with_Bonus
# 0  John   28   50000               55000
# 1  Jane   34   60000               65000
# 2   Tom   29   55000               60000
# 3  Lucy   31   70000               75000

# ---------------------------------------------------

# Define a custom function to combine Name and Age
def name_age_summary(row):
    return f"{row['Name']} is {row['Age']} years old"


# ?Why No axis Needed
#? Single Column Operation: Since you’re applying a function to a single column (which is a Series), apply() automatically operates element-wise. Each value in the Series is passed to the function, so specifying axis is unnecessary.

# ?DataFrame Context: The axis parameter is relevant when using apply() on a DataFrame because you need to specify whether the function should operate row-wise (axis=1) or column-wise (axis=0). For a Series, this distinction isn’t needed because it’s inherently one-dimensional.

# Apply the custom function to each row
# ! ask nazil
df['Name_Age_Summary'] = df.apply(name_age_summary, axis=1)

print("DataFrame with Name and Age Summary:")
print(df)
# Output:
# DataFrame with Name and Age Summary:
#    Name  Age  Salary  Salary_with_Bonus                Name_Age_Summary
# 0  John   28   50000               55000   John is 28 years old
# 1  Jane   34   60000               65000   Jane is 34 years old
# 2   Tom   29   55000               60000    Tom is 29 years old
# 3  Lucy   31   70000               75000   Lucy is 31 years old

# ---------------------------------------------------

# Define a custom function to calculate the range (max - min) of a column
def range_of_column(column):
    return column.max() - column.min()

# Apply the custom function to each column
# ! ask nazil
column_ranges = df.apply(range_of_column, axis=0)

print("Range of Each Column:")
print(column_ranges)
# Output:
# Range of Each Column:
# Age                          6
# Salary                    20000
# Salary_with_Bonus         25000
# dtype: int64

# ============================================================

# Using .transform() for element-wise transformations.

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Tom', 'Lucy'],
    'Age': [28, 34, 29, 31],
    'Salary': [50000, 60000, 55000, 70000]
}

df = pd.DataFrame(data)

# ---------------------------------------------------

# Define a function that transforms each value by adding 10%
def add_percentage(value):
    return value * 1.10

# Apply the function to the 'Salary' column using .transform()
df['Salary_with_Percentage'] = df['Salary'].transform(add_percentage)

print("DataFrame with Salary Increased by 10%:")
print(df)
# Output:
# DataFrame with Salary Increased by 10%:
#    Name  Age  Salary  Salary_with_Percentage
# 0  John   28   50000                 55000.0
# 1  Jane   34   60000                 66000.0
# 2   Tom   29   55000                 60500.0
# 3  Lucy   31   70000                 77000.0

# ---------------------------------------------------

# Define a function that standardizes each value by subtracting the mean and dividing by the standard deviation

# df['Age'].transform(standardize) applies the standardize() function to each value in the 'Age' column.
# The value parameter inside standardize() refers to a single value (one element) at a time from the 'Age' column.
# The calculations for mean and std are performed once for the entire column, but the function is called repeatedly for each value, and each value is standardized individually.

def standardize(value):
    mean = df['Age'].mean()
    std = df['Age'].std()
    return (value - mean) / std

# Apply the function to the 'Age' column using .transform()
df['Age_Standardized'] = df['Age'].transform(standardize)

print("DataFrame with Age Standardized:")
print(df)
# Output:
# DataFrame with Age Standardized:
#    Name  Age  Salary  Salary_with_Percentage  Age_Standardized
# 0  John   28   50000                 55000.0         -1.348399
# 1  Jane   34   60000                 66000.0          0.674199
# 2   Tom   29   55000                 60500.0         -0.337100
# 3  Lucy   31   70000                 77000.0          0.011799

# ---------------------------------------------------

# Define a function that calculates the cumulative sum of a column
def cumulative_sum(value):
    return value.cumsum()

# Apply the function to the 'Salary' column using .transform()
df['Salary_Cumulative'] = df['Salary'].transform(cumulative_sum)

print("DataFrame with Cumulative Salary:")
print(df)
# Output:
# DataFrame with Cumulative Salary:
#    Name  Age  Salary  Salary_with_Percentage  Age_Standardized  Salary_Cumulative
# 0  John   28   50000                 55000.0         -1.348399              50000
# 1  Jane   34   60000                 66000.0          0.674199             110000
# 2   Tom   29   55000                 60500.0         -0.337100             165000
# 3  Lucy   31   70000                 77000.0          0.011799             235000

# ===================================================================================================

# Advanced filtering with multiple conditions.

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Tom', 'Lucy', 'Mike'],
    'Age': [28, 34, 29, 31, 45],
    'Salary': [50000, 60000, 55000, 70000, 48000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
# Output:
# Original DataFrame:
#    Name  Age  Salary Department
# 0  John   28   50000         HR
# 1  Jane   34   60000         IT
# 2   Tom   29   55000    Finance
# 3  Lucy   31   70000         IT
# 4  Mike   45   48000    Finance

# ---------------------------------------------------

# Filtering with multiple conditions:
# 1. Age greater than 30
# 2. Salary greater than 50000
# 3. Department is 'IT' or 'Finance'

filtered_df = df[(df['Age'] > 30) & (df['Salary'] > 50000) & (df['Department'].isin(['IT', 'Finance']))]

print("Filtered DataFrame (Age > 30, Salary > 50000, Department in ['IT', 'Finance']):")
print(filtered_df)
# Output:
# Filtered DataFrame (Age > 30, Salary > 50000, Department in ['IT', 'Finance']):
#    Name  Age  Salary Department
# 1  Jane   34   60000         IT
# 3  Lucy   31   70000         IT
# 4  Mike   45   48000    Finance

# ---------------------------------------------------

# Additional filtering example:
# 1. Age between 25 and 35
# 2. Salary less than 60000

additional_filtered_df = df[(df['Age'].between(25, 35)) & (df['Salary'] < 60000)]

print("Additional Filtered DataFrame (Age between 25 and 35, Salary < 60000):")
print(additional_filtered_df)
# Output:
# Additional Filtered DataFrame (Age between 25 and 35, Salary < 60000):
#    Name  Age  Salary Department
# 0  John   28   50000         HR
# 2   Tom   29   55000    Finance
# 3  Lucy   31   70000         IT

# ---------------------------------------------------

# Filtering using OR conditions
# 1. Age less than 30 or Salary greater than 65000

or_filtered_df = df[(df['Age'] < 30) | (df['Salary'] > 65000)]

print("Filtered DataFrame (Age < 30 OR Salary > 65000):")
print(or_filtered_df)
# Output:
# Filtered DataFrame (Age < 30 OR Salary > 65000):
#    Name  Age  Salary Department
# 0  John   28   50000         HR
# 3  Lucy   31   70000         IT
# 4  Mike   45   48000    Finance

# =============================================================================================

# Working with multi-indexed DataFrames.

import pandas as pd

# Creating a DataFrame with a multi-index
data = {
    'Sales': [200, 220, 250, 300, 320, 400],
    'Profit': [20, 30, 35, 40, 45, 55]
}

index = pd.MultiIndex.from_tuples(
    [('2023-Q1', 'North'), ('2023-Q1', 'South'), 
     ('2023-Q2', 'North'), ('2023-Q2', 'South'),
     ('2023-Q3', 'North'), ('2023-Q3', 'South')],
    names=['Quarter', 'Region']
)

df = pd.DataFrame(data, index=index)

print("Original Multi-Indexed DataFrame:")
print(df)
# Output:
# Original Multi-Indexed DataFrame:
#                   Sales  Profit
# Quarter  Region                
# 2023-Q1 North     200      20
#         South     220      30
# 2023-Q2 North     250      35
#         South     300      40
# 2023-Q3 North     320      45
#         South     400      55

# ---------------------------------------------------

# Accessing data at a specific level
# Accessing all data for '2023-Q1'
q1_data = df.loc['2023-Q1']
print("\nData for '2023-Q1':")
print(q1_data)
# Output:
# Data for '2023-Q1':
#           Sales  Profit
# Region                
# North     200      20
# South     220      30

# ---------------------------------------------------

# Accessing data using multiple levels
# Accessing data for '2023-Q2' and 'North'
q2_north_data = df.loc[('2023-Q2', 'North')]
print("\nData for '2023-Q2' and 'North':")
print(q2_north_data)
# Output:
# Data for '2023-Q2' and 'North':
# Sales     250
# Profit     35
# Name: (2023-Q2, North), dtype: int64

# ---------------------------------------------------

# Slicing with multi-index
# Slicing data for all quarters in the 'North' region
north_data = df.xs('North', level='Region')
print("\nData for 'North' Region across all quarters:")
print(north_data)
# Output:
# Data for 'North' Region across all quarters:
#           Sales  Profit
# Quarter                
# 2023-Q1    200      20
# 2023-Q2    250      35
# 2023-Q3    320      45

# ---------------------------------------------------

# Resetting the index
# Resetting the multi-index to a single index
df_reset = df.reset_index()
print("\nDataFrame with Multi-Index Reset:")
print(df_reset)
# Output:
# DataFrame with Multi-Index Reset:
#    Quarter Region  Sales  Profit
# 0  2023-Q1  North    200      20
# 1  2023-Q1  South    220      30
# 2  2023-Q2  North    250      35
# 3  2023-Q2  South    300      40
# 4  2023-Q3  North    320      45
# 5  2023-Q3  South    400      55

# ---------------------------------------------------

# Setting a new multi-index
# Setting 'Quarter' and 'Region' as a new multi-index
df_new_index = df_reset.set_index(['Quarter', 'Region'])
print("\nDataFrame with New Multi-Index:")
print(df_new_index)
# Output:
# DataFrame with New Multi-Index:
#                   Sales  Profit
# Quarter  Region                
# 2023-Q1 North     200      20
#         South     220      30
# 2023-Q2 North     250      35
#         South     300      40
# 2023-Q3 North     320      45
#         South     400      55

# ================================================================