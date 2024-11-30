# 1. apply() Method
# The apply() method allows you to apply a function along an axis (rows or columns) of a DataFrame or to a Series.

import pandas as pd

# Creating a DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Applying a function to each column (axis=0)
def add_one(x):
    return x + 1

df_apply = df.apply(add_one)

print(df_apply)
# Output:
#    A  B
# 0  2  5
# 1  3  6
# 2  4  7

# ---------------------------------------------------

# Applying a function to each row (axis=1)
def row_sum(row):
    return row.sum()

df_row_sum = df.apply(row_sum, axis=1)

print(df_row_sum)
# Output:
# 0     5
# 1     7
# 2     9
# dtype: int64
# -----------------------------------------------------------------------------------------------------------

# 2. map() Method
# The map() method is used for element-wise transformations on a Series. It applies a function or mapping correspondence to each element of the Series.

import pandas as pd

# Creating a Series
s = pd.Series([1, 2, 3, 4])

# Mapping a function to each element
def square(x):
    return x ** 2

s_map = s.map(square)

print(s_map)
# Output:
# 0     1
# 1     4
# 2     9
# 3    16
# dtype: int64

# ---------------------------------------------------

# Using a dictionary for mapping
mapping_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
s_map_dict = s.map(mapping_dict)

print(s_map_dict)
# Output:
# 0    A
# 1    B
# 2    C
# 3    D
# dtype: object

# -----------------------------------------------------------------------------------------------------------

# 3. Lambda Functions
# Lambda functions are anonymous functions defined using the lambda keyword. They are useful for small, one-off functions.

import pandas as pd

# Creating a DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Applying a lambda function to each column
df_lambda = df.apply(lambda x: x + 1)

print(df_lambda)
# Output:
#    A  B
# 0  2  5
# 1  3  6
# 2  4  7

# ---------------------------------------------------

# Applying a lambda function to each row
df_row_lambda = df.apply(lambda row: row['A'] + row['B'], axis=1)

print(df_row_lambda)
# Output:
# 0     5
# 1     7
# 2     9
# dtype: int64
