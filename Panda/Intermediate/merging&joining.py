import pandas as pd

# Concat method

# Creating two DataFrames for demonstration
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
})

# Row-wise concatenation (default axis=0)


# The ignore_index=True parameter in pd.concat([df1, df2], ignore_index=True) is used to reset the index when concatenating multiple DataFrames along rows. By default, when concatenating, pandas keeps the original row indices from the source DataFrames. Setting ignore_index=True tells pandas to disregard the existing row indices and create a new default integer index for the resulting DataFrame.

df_concat_rows = pd.concat([df1, df2], ignore_index=True)
print("Row-wise Concatenation:\n", df_concat_rows)
# Output:
# Row-wise Concatenation:
#     A   B   C   D
# 0  A0  B0  C0  D0
# 1  A1  B1  C1  D1
# 2  A2  B2  C2  D2
# 3  A3  B3  C3  D3
# 4  A4  B4  C4  D4
# 5  A5  B5  C5  D5
# 6  A6  B6  C6  D6
# 7  A7  B7  C7  D7

# ----------------------------------------

# Creating two DataFrames with different columns for column-wise concatenation
df3 = pd.DataFrame({
    'E': ['E0', 'E1', 'E2', 'E3'],
    'F': ['F0', 'F1', 'F2', 'F3']
})

# Column-wise concatenation (axis=1)
df_concat_cols = pd.concat([df1, df3], axis=1)
print("\nColumn-wise Concatenation:\n", df_concat_cols)
# Output:
# Column-wise Concatenation:
#     A   B   C   D   E   F
# 0  A0  B0  C0  D0  E0  F0
# 1  A1  B1  C1  D1  E1  F1
# 2  A2  B2  C2  D2  E2  F2
# 3  A3  B3  C3  D3  E3  F3

# ----------------------------------------

# Concatenating with missing values (mismatched indexes)
df4 = pd.DataFrame({
    'A': ['A8', 'A9'],
    'B': ['B8', 'B9'],
    'C': ['C8', 'C9'],
    'D': ['D8', 'D9']
}, index=[8, 9])

df_concat_mismatch = pd.concat([df1, df4])
print("\nRow-wise Concatenation with Mismatched Indexes:\n", df_concat_mismatch)
# Output:
# Row-wise Concatenation with Mismatched Indexes:
#      A   B   C   D
# 0   A0  B0  C0  D0
# 1   A1  B1  C1  D1
# 2   A2  B2  C2  D2
# 3   A3  B3  C3  D3
# 8   A8  B8  C8  D8
# 9   A9  B9  C9  D9

# ===============================================================================================

# Joining Method

import pandas as pd

# Creating two DataFrames with a common column "ID"
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Jane', 'Tom', 'Anna']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [29, 32, 28, 40]
})

print("DataFrame 1 (df1):\n", df1)
# Output:
# DataFrame 1 (df1):
#    ID   Name
# 0   1   John
# 1   2   Jane
# 2   3    Tom
# 3   4   Anna

print("\nDataFrame 2 (df2):\n", df2)
# Output:
# DataFrame 2 (df2):
#    ID  Age
# 0   3   29
# 1   4   32
# 2   5   28
# 3   6   40

# ----------------------------------------

# 1. Inner Join (default) - Only keeps rows with matching keys in both DataFrames
df_inner = pd.merge(df1, df2, how='inner', on='ID')
print("\nInner Join (df1 and df2 on ID):\n", df_inner)
# Output:
# Inner Join (df1 and df2 on ID):
#    ID  Name  Age
# 0   3   Tom   29
# 1   4  Anna   32

# ----------------------------------------

# 2. Left Join - Keeps all rows from the left DataFrame (df1), and matches with df2 where possible
df_left = pd.merge(df1, df2, how='left', on='ID')
print("\nLeft Join (df1 and df2 on ID):\n", df_left)
# Output:
# Left Join (df1 and df2 on ID):
#    ID   Name   Age
# 0   1   John   NaN
# 1   2   Jane   NaN
# 2   3    Tom  29.0
# 3   4   Anna  32.0

# ----------------------------------------

# 3. Right Join - Keeps all rows from the right DataFrame (df2), and matches with df1 where possible
df_right = pd.merge(df1, df2, how='right', on='ID')
print("\nRight Join (df1 and df2 on ID):\n", df_right)
# Output:
# Right Join (df1 and df2 on ID):
#    ID   Name  Age
# 0   3    Tom   29
# 1   4   Anna   32
# 2   5    NaN   28
# 3   6    NaN   40

# ----------------------------------------

# 4. Outer Join - Keeps all rows from both DataFrames, filling NaN where there is no match
df_outer = pd.merge(df1, df2, how='outer', on='ID')
print("\nOuter Join (df1 and df2 on ID):\n", df_outer)
# Output:
# Outer Join (df1 and df2 on ID):
#    ID   Name   Age
# 0   1   John   NaN
# 1   2   Jane   NaN
# 2   3    Tom  29.0
# 3   4   Anna  32.0
# 4   5    NaN  28.0
# 5   6    NaN  40.0

# ==========================================================================================================

# Join by the index method

import pandas as pd

# Creating two DataFrames with matching indexes
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Tom', 'Anna'],
    'Age': [28, 34, 29, 32]
}, index=[1, 2, 3, 4])

df2 = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer']
}, index=[1, 2, 3, 4])

print("DataFrame 1 (df1):\n", df1)
# Output:
# DataFrame 1 (df1):
#     Name  Age
# 1   John   28
# 2   Jane   34
# 3    Tom   29
# 4   Anna   32

print("\nDataFrame 2 (df2):\n", df2)
# Output:
# DataFrame 2 (df2):
#              City Occupation
# 1      New York   Engineer
# 2   Los Angeles     Doctor
# 3       Chicago     Artist
# 4       Houston     Lawyer

# ----------------------------------------------------

# 1. Left Join by default (Join based on indexes)
df_join_left = df1.join(df2)
print("\nLeft Join by Index (df1 joined with df2):\n", df_join_left)
# Output:
# Left Join by Index (df1 joined with df2):
#     Name  Age         City Occupation
# 1   John   28     New York   Engineer
# 2   Jane   34  Los Angeles     Doctor
# 3    Tom   29      Chicago     Artist
# 4   Anna   32      Houston     Lawyer

# ----------------------------------------------------

# 2. Right Join - Keeping all rows from df2 and matching with df1
df_join_right = df1.join(df2, how='right')
print("\nRight Join by Index (df1 joined with df2):\n", df_join_right)
# Output:
# Right Join by Index (df1 joined with df2):
#     Name  Age         City Occupation
# 1   John   28     New York   Engineer
# 2   Jane   34  Los Angeles     Doctor
# 3    Tom   29      Chicago     Artist
# 4   Anna   32      Houston     Lawyer

# ----------------------------------------------------

# 3. Outer Join - Keeping all rows from both DataFrames, filling with NaN where no match
df_join_outer = df1.join(df2, how='outer')
print("\nOuter Join by Index (df1 joined with df2):\n", df_join_outer)
# Output:
# Outer Join by Index (df1 joined with df2):
#     Name   Age         City Occupation
# 1   John  28.0     New York   Engineer
# 2   Jane  34.0  Los Angeles     Doctor
# 3    Tom  29.0      Chicago     Artist
# 4   Anna  32.0      Houston     Lawyer

# ----------------------------------------------------

# 4. Inner Join - Keeping only the common rows in both DataFrames based on indexes
df_join_inner = df1.join(df2, how='inner')
print("\nInner Join by Index (df1 joined with df2):\n", df_join_inner)
# Output:
# Inner Join by Index (df1 joined with df2):
#     Name  Age         City Occupation
# 1   John   28     New York   Engineer
# 2   Jane   34  Los Angeles     Doctor
# 3    Tom   29      Chicago     Artist
# 4   Anna   32      Houston     Lawyer
