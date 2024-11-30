import pandas as pd

# Creating a sample DataFrame
data = {
    'Old_Name1': [10, 20, 30],
    'Old_Name2': [40, 50, 60],
    'Old_Name3': [70, 80, 90]
}

df = pd.DataFrame(data, index=['Row1', 'Row2', 'Row3'])

print("Original DataFrame:")
print(df)

# ---------------------------------------------------

# 1. Renaming Columns

# Define new column names
new_column_names = {
    'Old_Name1': 'New_Name1',
    'Old_Name2': 'New_Name2',
    'Old_Name3': 'New_Name3'
}

# Apply the .rename() method to rename columns
df_renamed_columns = df.rename(columns=new_column_names)

print("\nDataFrame with Renamed Columns:")
print(df_renamed_columns)
# Output:
#       New_Name1  New_Name2  New_Name3
# Row1         10         40         70
# Row2         20         50         80
# Row3         30         60         90

# ---------------------------------------------------

# 2. Renaming Rows

# Define new row names
new_row_names = {
    'Row1': 'First_Row',
    'Row2': 'Second_Row',
    'Row3': 'Third_Row'
}

# Apply the .rename() method to rename rows
df_renamed_rows = df.rename(index=new_row_names)

print("\nDataFrame with Renamed Rows:")
print(df_renamed_rows)
# Output:
#            Old_Name1  Old_Name2  Old_Name3
# First_Row         10         40         70
# Second_Row        20         50         80
# Third_Row         30         60         90

# ---------------------------------------------------

# 3. Renaming Both Columns and Rows

# Define new column and row names
new_names = {
    'columns': {
        'Old_Name1': 'New_Col1',
        'Old_Name2': 'New_Col2',
        'Old_Name3': 'New_Col3'
    },
    'index': {
        'Row1': 'First_Row',
        'Row2': 'Second_Row',
        'Row3': 'Third_Row'
    }
}

# Apply the .rename() method to rename both columns and rows
df_renamed_both = df.rename(columns=new_names['columns'], index=new_names['index'])

print("\nDataFrame with Renamed Columns and Rows:")
print(df_renamed_both)
# Output:
#            New_Col1  New_Col2  New_Col3
# First_Row        10        40        70
# Second_Row       20        50        80
# Third_Row        30        60        90

# -------------------------------------------------------------------------------------------------

# Example: Renaming a Specific Column

import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ---------------------------------------------------

# Renaming column 'B' to 'New_B'
df_renamed = df.rename(columns={'B': 'New_B'})

print("\nDataFrame after renaming column 'B' to 'New_B':")
print(df_renamed)

# Output:
#    A  New_B  C
# 0  1      4  7
# 1  2      5  8
# 2  3      6  9
    