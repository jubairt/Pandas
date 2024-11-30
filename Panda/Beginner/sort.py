# sort_values():

# You can sort the DataFrame by a specific column ('Age' or 'Score').
# You can specify whether to sort in ascending or descending order.


# 1. sort_values() Method
# The .sort_values() method is used to sort a DataFrame by one or more columns' values.

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Jubair', 'Jabir', 'Aisha', 'Fatima'],
    'Age': [34, 54, 22, 30],
    'Score': [85, 90, 95, 88]
}

df = pd.DataFrame(data)

# Sorting by Age in ascending order
df_sorted_age = df.sort_values(by='Age')

print(df_sorted_age)
# Output:
#      Name  Age  Score
# 2   Aisha   22     95
# 3  Fatima   30     88
# 0  Jubair   34     85
# 1   Jabir   54     90

# ---------------------------------------------------

# Sorting by Score in descending order
df_sorted_score = df.sort_values(by='Score', ascending=False)

print(df_sorted_score)
# Output:
#      Name  Age  Score
# 2   Aisha   22     95
# 1   Jabir   54     90
# 3  Fatima   30     88
# 0  Jubair   34     85

# --------------------------------------------------------------------------------------


# sort_index():

# Sorts by the index (row or column index).
# You can sort row indices (axis=0) or column names (axis=1) in ascending or descending order.

# 2. sort_index() Method
# The .sort_index() method is used to sort a DataFrame by its index, either row-wise or column-wise.

import pandas as pd

# Creating a DataFrame with custom row indices
data = {
    'Name': ['Jubair', 'Jabir', 'Aisha', 'Fatima'],
    'Age': [34, 54, 22, 30],
    'Score': [85, 90, 95, 88]
}

df = pd.DataFrame(data, index=[2, 0, 3, 1])

# Sorting by row index in ascending order
df_sorted_index = df.sort_index()

print(df_sorted_index)
# Output:
#      Name  Age  Score
# 0   Jabir   54     90
# 1  Fatima   30     88
# 2  Jubair   34     85
# 3   Aisha   22     95

# ---------------------------------------------------

# Sorting columns alphabetically by column index
df_sorted_columns = df.sort_index(axis=1)

print(df_sorted_columns)
# Output:
#      Age  Name  Score
# 2    34  Jubair     85
# 0    54   Jabir     90
# 3    22   Aisha     95
# 1    30  Fatima     88
