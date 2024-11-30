import pandas as pd

# 1. Handling Conversion Errors with .astype()

# Sample DataFrame with mixed data
data = {
    'A': ['1', '2', 'three', '4'],
    'B': ['5', 'six', '7', '8']
}

df = pd.DataFrame(data)"Original DataFrame:")
print(df)

# ---------------------------------------------------

# Handling errors during conversion (e.g., converting column 'A' to int)
# Setting errors='ignore' means invalid conversions will be ignored
df['A'] = df['A'].astype(int, errors='ignore')

# Handling errors by coercing (invalid parsing will become NaN)
df['B'] = pd.to_numeric(df['B'], errors='coerce')

print("\nDataFrame after attempting conversions:")
print(df)

# Output:
#      A    B
# 0    1  5.0
# 1    2  NaN
# 2  three  7.0
# 3    4  8.0

# ----------------------------------------------------------------------------------------------

# 2. Handling Non-Numeric Data Using pd.to_numeric()

import pandas as pd

# Sample DataFrame with strings and numbers
data = {
    'numbers': ['1', '2', 'invalid', '4'],
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ---------------------------------------------------

# Convert to numeric using pd.to_numeric() with errors='coerce' (invalid entries become NaN)
df['numbers'] = pd.to_numeric(df['numbers'], errors='coerce')

print("\nDataFrame after converting to numeric:")
print(df)

# Output:
#    numbers
# 0      1.0
# 1      2.0
# 2      NaN
# 3      4.0

# ----------------------------------------------------------------------------------------------------------

# 3. Working with Categorical Data using .astype('category')

import pandas as pd

# Sample DataFrame with categorical-like data
data = {
    'Fruit': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana'],
    'Quantity': [10, 15, 10, 5, 15]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ---------------------------------------------------

# Convert the 'Fruit' column to category
df['Fruit'] = df['Fruit'].astype('category')

print("\nDataFrame after converting 'Fruit' to category:")
print(df)
print("\nData Types After Conversion:")
print(df.dtypes)

# Output:
#      Fruit  Quantity
# 0    Apple        10
# 1   Banana        15
# 2    Apple        10
# 3   Orange         5
# 4   Banana        15
# Fruit       category
# Quantity       int64

# ---------------------------------------------------------------------------------------------

# 4. Datetime Components and Operations with pd.to_datetime()

import pandas as pd

# Sample DataFrame with date strings
data = {
    'Date': ['2024-08-28', '2023-05-15', '2022-12-01'],
}

df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

print("Original DataFrame with Datetime:")
print(df)

# ---------------------------------------------------

# Extract year, month, and day from the datetime column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Perform a date calculation (difference from today)
df['Days_Since'] = (pd.Timestamp('today') - df['Date']).dt.days

print("\nDataFrame with Date Components and Calculations:")
print(df)

# Output:
#         Date  Year  Month  Day  Days_Since
# 0 2024-08-28  2024      8   28       -365
# 1 2023-05-15  2023      5   15        -25
# 2 2022-12-01  2022     12    1        330
