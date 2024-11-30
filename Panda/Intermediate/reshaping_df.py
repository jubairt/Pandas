# Stacking and unstacking data with .stack() and .unstack().

import pandas as pd

# Creating a sample DataFrame
data = {
    'Year': [2021, 2021, 2022, 2022],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb'],
    'Sales': [250, 300, 350, 400]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Output:
# Original DataFrame:
#    Year Month  Sales
# 0  2021   Jan    250
# 1  2021   Feb    300
# 2  2022   Jan    350
# 3  2022   Feb    400

# Setting 'Year' and 'Month' as a multi-index
df_indexed = df.set_index(['Year', 'Month'])
print("\nDataFrame with Multi-Index:")
print(df_indexed)
# Output:
# DataFrame with Multi-Index:
#              Sales
# Year Month       
# 2021 Jan    250
#      Feb    300
# 2022 Jan    350
#      Feb    400

# ---------------------------------------------------

# Stacking: Converts columns to rows
stacked = df_indexed.stack()
print("\nStacked DataFrame:")
print(stacked)
# Output:
# Stacked DataFrame:
# Year  Month    
# 2021  Jan    Sales    250
#       Feb    Sales    300
# 2022  Jan    Sales    350
#       Feb    Sales    400
# dtype: int64

# ---------------------------------------------------

# Unstacking: Converts rows back to columns
unstacked = stacked.unstack()
print("\nUnstacked DataFrame:")
print(unstacked)
# Output:
# Unstacked DataFrame:
# Month   Jan  Feb
# Year          
# 2021   250  300
# 2022   350  400

# =============================================================================================

# Pivot tables with .pivot() and .pivot_table().

import pandas as pd

# Creating a sample DataFrame
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [55, 75, 60, 80]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Output:
# Original DataFrame:
#         Date         City  Temperature
# 0  2024-01-01    New York           55
# 1  2024-01-01  Los Angeles           75
# 2  2024-01-02    New York           60
# 3  2024-01-02  Los Angeles           80

# Pivoting the DataFrame
pivoted = df.pivot(index='Date', columns='City', values='Temperature')
print("\nPivoted DataFrame using .pivot():")
print(pivoted)
# Output:
# Pivoted DataFrame using .pivot():
# City        Los Angeles  New York
# Date                           
# 2024-01-01           75        55
# 2024-01-02           80        60

# ---------------------------------------------------

# Using .pivot_table()

import pandas as pd

# Creating a sample DataFrame with duplicate entries
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-01'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York'],
    'Temperature': [55, 75, 60, 80, 65]
}

df = pd.DataFrame(data)
print("Original DataFrame with Duplicates:")
print(df)
# Output:
# Original DataFrame with Duplicates:
#         Date         City  Temperature
# 0  2024-01-01    New York           55
# 1  2024-01-01  Los Angeles           75
# 2  2024-01-02    New York           60
# 3  2024-01-02  Los Angeles           80
# 4  2024-01-01    New York           65

# Pivoting with aggregation
pivot_table = df.pivot_table(index='Date', columns='City', values='Temperature', aggfunc='mean')
print("\nPivot Table using .pivot_table():")
print(pivot_table)
# Output:
# Pivot Table using .pivot_table():
# City        Los Angeles  New York
# Date                           
# 2024-01-01           75      60.0
# 2024-01-02           80      60.0


# ==============================================================================

# Melting DataFrames with .melt().

import pandas as pd

# Creating a sample DataFrame
data = {
    'Date': ['2024-01-01', '2024-01-02'],
    'New York_Temperature': [55, 60],
    'Los_Angeles_Temperature': [75, 80]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Output:
# Original DataFrame:
#         Date  New York_Temperature  Los_Angeles_Temperature
# 0  2024-01-01                    55                       75
# 1  2024-01-02                    60                       80

# Melting the DataFrame
melted_df = df.melt(id_vars='Date', 
                    var_name='City_Temperature', 
                    value_name='Temperature')

print("\nMelted DataFrame using .melt():")
print(melted_df)
# Output:
# Melted DataFrame using .melt():
#         Date           City_Temperature  Temperature
# 0  2024-01-01       New York_Temperature           55
# 1  2024-01-02       New York_Temperature           60
# 2  2024-01-01  Los_Angeles_Temperature           75
# 3  2024-01-02  Los_Angeles_Temperature           80

# ======================================================================================