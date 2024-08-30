import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22],
    'Score': [85, 92, 78]
}

df = pd.DataFrame(data)
print(df)
# Output:
#     Name  Age  Score
# 0   John   25     85
# 1  Alice   30     92
# 2    Bob   22     78

# ---------------------------------------------

# df.head(): This function returns the first 5 rows of the DataFrame df by default.
# You can pass an integer as an argument to the head() function to display a different number of rows. For example, df.head(3) would return the first 3 rows.
print(df.head())
# Output:
#     Name  Age  Score
# 0   John   25     85
# 1  Alice   30     92
# 2    Bob   22     78

# ---------------------------------------------

# The tail() function is used to view the last few rows of a DataFrame or Series. By default, it shows the last 5 rows, but you can specify a different number if needed.

print(df.tail(2))

#     Name  Age  Score
# 1  Alice   30     92
# 2    Bob   22     78

# -----------------------------------------------

# Display basic information about the DataFrame
print(df.info())
# Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   Name    3 non-null      object
#  1   Age     3 non-null      int64 
#  2   Score   3 non-null      int64 
# dtypes: int64(2), object(1)
# memory usage: 200.0+ bytes

# ---------------------------------------------

# Display statistical summary of numerical columns
print(df.describe())
# Output:
#              Age     Score
# count   3.000000   3.00000
# mean   25.666667  85.00000
# std     4.041241   7.00000
# min    22.000000  78.00000
# 25%    23.500000  81.50000
# 50%    25.000000  85.00000
# 75%    27.500000  88.50000
# max    30.000000  92.00000

# ---------------------------------------------

# Access a specific column (as a Series)
print(df['Age'])
# Output:
# 0    25
# 1    30
# 2    22
# Name: Age, dtype: int64

# ---------------------------------------------

# Access a specific row by index (using .loc)
print(df.loc[1])
# Output:
# Name     Alice
# Age         30
# Score       92
# Name: 1, dtype: object

# ---------------------------------------------

# Add a new column based on a condition
df['Pass'] = df['Score'] > 80
print(df)
# Output:
#     Name  Age  Score   Pass
# 0   John   25     85   True
# 1  Alice   30     92   True
# 2    Bob   22     78  False

# ---------------------------------------------

# Filter rows where Pass is True
passed_students = df[df['Pass'] == True]
print(passed_students)
# Output:
#     Name  Age  Score   Pass
# 0   John   25     85   True
# 1  Alice   30     92   True

# ---------------------------------------------

# Sort the DataFrame by Score in descending order
df_sorted = df.sort_values(by='Score', ascending=False)
print(df_sorted)
# Output:
#     Name  Age  Score   Pass
# 1  Alice   30     92   True
# 0   John   25     85   True
# 2    Bob   22     78  False


# ---------------------------------------------------------------------

# Creating a DataFrame from a list of lists
data = [
    ['John', 25, 85],
    ['Alice', 30, 92],
    ['Bob', 22, 78]
]

# Specifying column names
columns = ['Name', 'Age', 'Score']

df = pd.DataFrame(data, columns=columns)

print(df)
# Output:
#     Name  Age  Score
# 0   John   25     85
# 1  Alice   30     92
# 2    Bob   22     78

# ---------------------------------------------------------------------

# Creating DataFrames from Series
names = pd.Series(['John', 'Alice', 'Bob'], name='Name')
ages = pd.Series([25, 30, 22], name='Age')
scores = pd.Series([85, 92, 78], name='Score')

# Combining Series into a DataFrame
df = pd.concat([names, ages, scores], axis=1)

print(df)
# Output:
#     Name  Age  Score
# 0   John   25     85
# 1  Alice   30     92
# 2    Bob   22     78


# ---------------------------------------------------------------------

# Creating a DataFrame from a list of tuples
data_tuples = [
    ('John', 25, 85),
    ('Alice', 30, 92),
    ('Bob', 22, 78)
]

columns = ['Name', 'Age', 'Score']

df_tuples = pd.DataFrame(data_tuples, columns=columns)

print(df_tuples)
# Output:
#     Name  Age  Score
# 0   John   25     85
# 1  Alice   30     92
# 2    Bob   22     78


# ---------------------------------------------------------------------

# Assuming a CSV file named 'data.csv' with the following content:
# Name,Age,Score
# John,25,85
# Alice,30,92
# Bob,22,78

# Reading a DataFrame from a CSV file
df_csv = pd.read_csv('data.csv')

print(df_csv)
# Output (assuming 'data.csv' contains the data above):
#     Name  Age  Score
# 0   John   25     85
# 1  Alice   30     92
# 2    Bob   22     78


# ---------------------------------------------------------------------

# 4. Creating a DataFrame from Excel Files
# You can create a DataFrame by reading data from Excel files using pandas.

# Example: Reading a DataFrame from an Excel File

# Assuming an Excel file named 'data.xlsx' with a sheet named 'Sheet1' containing the following data:
# Name  Age  Score
# John   25     85
# Alice  30     92
# Bob    22     78

# Reading a DataFrame from an Excel file
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')

print(df_excel)
# Output (assuming 'data.xlsx' contains the data above):
#     Name  Age  Score
# 0   John   25     85
# 1  Alice   30     92
# 2    Bob   22     78


# ---------------------------------------------------------------------

# Accessing Data in a DataFrame
# 1. Accessing Columns
# You can access columns in a DataFrame using the column name.

# Accessing a single column
print(df['Name'])
# Output:
# 0    John
# 1   Alice
# 2     Bob
# Name: Name, dtype: object

# Accessing multiple columns
print(df[['Name', 'Score']])
# Output:
#     Name  Score
# 0   John     85
# 1  Alice     92
# 2    Bob     78

# ---------------

# 2. Accessing Rows
# You can access rows by their index position or label using .loc[] or .iloc[].
# Accessing a row by index label (default integer index)
print(df.loc[1])
# Output:
# Name     Alice
# Age         30
# Score       92
# Name: 1, dtype: object

# Accessing a row by integer position
print(df.iloc[1])
# Output:
# Name     Alice
# Age         30
# Score       92
# Name: 1, dtype: object


# ---------------------------------------------------------------------

