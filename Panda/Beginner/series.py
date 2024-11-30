import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40]
ser = pd.Series(data)

print(ser)
# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# ---------------------------------------------

# Creating a Series with custom index labels
ser_custom = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(ser_custom)
# Output:
# a    10
# b    20
# c    30
# d    40
# dtype: int64

# ---------------------------------------------

# Accessing an element using the index label
print(ser_custom['b'])  
# Output:
# 20

# ---------------------------------------------

# Slicing the first two elements
print(ser_custom[:2])
# Output:
# 0    10
# 1    20
# dtype: int64


# ---------------------------------------------

# Function
# Applying a function to each element using .apply()
def add_ten(x):
    return x + 10

ser_applied = ser_custom(add_ten)
print(ser_applied)
# Output:
# 0    20
# 1    35
# 2    40
# 3    50
# dtype: int64


# ---------------------------------------------

# Add 5 to each element in the Series
ser_plus_5 = ser_custom + 5
print(ser_plus_5)
# Output:
# a    15
# b    25
# c    35
# d    45
# dtype: int64

# --------------------------------------------------------------------------------------------------------------

# Creating a Series from a dictionary
data_dict = {
    'John': 85,
    'Alice': 92,
    'Bob': 78,
    'Eve': 88
}
ser_from_dict = pd.Series(data_dict)

print(ser_from_dict)
# Output:
# John     85
# Alice    92
# Bob      78
# Eve      88
# dtype: int64


# ---------------------------------------------------------------------------------------------------

# Creating a Series with some repeated values
data_series = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])

# Counting the occurrences of each unique value
print(data_series.value_counts())
# Output:
# banana    3
# apple     2
# orange    1
# dtype: int64

# ---------------------------------------------------------------------------------------------------

# Counting occurrences of unique values in the 'Name' column of the DataFrame
print(df['Name'].value_counts())
# Output:
# John       1
# Alice      1
# Bob        1
# Eve        1
# Charlie    1
# David      1
# dtype: int64

# ---------------------------------------------------------------------------------------------------
# Logical operations

ser = pd.Series([10, 20, 30, 40])
# Combining multiple logical conditions with & (AND) and | (OR)
ser_combined = (ser > 15) & (ser < 35)
print(ser_combined)
# Output:
# 0    False
# 1     True
# 2     True
# 3    False
# dtype: bool