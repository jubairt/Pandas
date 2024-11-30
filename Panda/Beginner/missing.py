import pandas as pd

# Creating a sample DataFrame with missing data
data = {
    'Name': ['John', 'Jane', 'Tom', None],
    'Age': [28, None, 30, 22],
    'City': ['New York', 'Los Angeles', None, 'Chicago']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane   NaN  Los Angeles
# 2    Tom  30.0          NaN
# 3   None  22.0      Chicago

# ---------------------------------------------------

# Identifying missing data with .isna() (True where values are NaN)
missing_data = df.isna()
print("\nMissing data identified with .isna():")
print(missing_data)
# Output:
#     Name    Age   City
# 0  False  False  False
# 1  False   True  False
# 2  False  False   True
# 3   True  False  False

# ---------------------------------------------------

# Identifying non-missing data with .notna() (True where values are not NaN)
non_missing_data = df.notna()
print("\nNon-missing data identified with .notna():")
print(non_missing_data)
# Output:
#     Name   Age   City
# 0   True  True   True
# 1   True  False  True
# 2   True  True  False
# 3  False  True   True


# ===========================================================================================================

# Creating a sample DataFrame with missing data
data = {
    'Name': ['John', 'Jane', 'Tom', 'Jake', 'Anna'],
    'Age': [28, None, 30, None, 25],
    'City': ['New York', None, 'Los Angeles', 'Chicago', None]
}

df = pd.DataFrame(data)
print("Original DataFrame with Missing Data:")
print(df)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane   NaN          NaN
# 2    Tom  30.0  Los Angeles
# 3   Jake   NaN      Chicago
# 4   Anna  25.0          NaN

# ---------------------------------------------------

# Filling missing data with a specific value (e.g., 'Unknown' for City and 0 for Age)
df_filled = df.fillna({'City': 'Unknown', 'Age': 0})
print("\nDataFrame with Missing Data Filled (specific value):")
print(df_filled)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane   0.0      Unknown
# 2    Tom  30.0  Los Angeles
# 3   Jake   0.0      Chicago
# 4   Anna  25.0      Unknown

# ---------------------------------------------------

# Forward Fill (ffill) - Fills NaN with the previous value
df_ffill = df.fillna(method='ffill')
print("\nDataFrame with Forward Fill (ffill):")
print(df_ffill)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane  28.0     New York
# 2    Tom  30.0  Los Angeles
# 3   Jake  30.0      Chicago
# 4   Anna  25.0      Chicago

# ---------------------------------------------------

# Backward Fill (bfill) - Fills NaN with the next value
df_bfill = df.fillna(method='bfill')
print("\nDataFrame with Backward Fill (bfill):")
print(df_bfill)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane  30.0  Los Angeles
# 2    Tom  30.0  Los Angeles
# 3   Jake  25.0      Chicago
# 4   Anna  25.0          NaN


# ===========================================================================================================

# Dropping missing data examples

df = pd.DataFrame(data)
print("Original DataFrame with Missing Data:")
print(df)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane   NaN          NaN
# 2    Tom  30.0  Los Angeles
# 3   Jake   NaN      Chicago
# 4   Anna  25.0          NaN

# ---------------------------------------------------

# Dropping rows with any missing data (default behavior)
df_drop_any = df.dropna()
print("\nDataFrame with rows dropped where any value is missing:")
print(df_drop_any)
# Output:
#    Name   Age         City
# 0  John  28.0     New York
# 2   Tom  30.0  Los Angeles

# ---------------------------------------------------

# Dropping rows where all values are missing
df_drop_all = df.dropna(how='all')
print("\nDataFrame with rows dropped where all values are missing:")
print(df_drop_all)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane   NaN          NaN
# 2    Tom  30.0  Los Angeles
# 3   Jake   NaN      Chicago
# 4   Anna  25.0          NaN

# ---------------------------------------------------

# Dropping columns with any missing data
df_drop_columns_any = df.dropna(axis=1)
print("\nDataFrame with columns dropped where any value is missing:")
print(df_drop_columns_any)
# Output:
#    Name
# 0  John
# 1  Jane
# 2   Tom
# 3  Jake
# 4  Anna

# ---------------------------------------------------

# Dropping rows with fewer than 2 non-missing values
df_drop_thresh = df.dropna(thresh=2)
print("\nDataFrame with rows dropped where fewer than 2 non-missing values are present:")
print(df_drop_thresh)
# Output:
#     Name   Age         City
# 0   John  28.0     New York
# 1   Jane   NaN          NaN
# 2    Tom  30.0  Los Angeles
# 3   Jake   NaN      Chicago
# 4   Anna  25.0          NaN

# ---------------------------------------------------

# Dropping rows based on specific columns (e.g., only check 'Age' column)
df_drop_subset = df.dropna(subset=['Age'])
print("\nDataFrame with rows dropped based on missing values in 'Age' column:")
print(df_drop_subset)
# Output:
#    Name   Age         City
# 0  John  28.0     New York
# 2   Tom  30.0  Los Angeles
# 4  Anna  25.0          NaN


# ===========================================================================================================


# Handling Outliers and Special Cases

# 1. Identifying Outliers Using IQR

data = {
    'Value': [10, 12, 14, 16, 18, 20, 22, 24, 100, 200]  # 100 and 200 are outliers
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Output:
#    Value
# 0     10
# 1     12
# 2     14
# 3     16
# 4     18
# 5     20
# 6     22
# 7     24
# 8    100
# 9    200

# ---------------------------------------------------

# Calculating IQR to identify outliers
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1

# Defining outlier thresholds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nIQR Calculations:")
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
# Output:
# Q1: 15.0, Q3: 22.0, IQR: 7.0
# Lower Bound: 1.5, Upper Bound: 35.5

# Identifying outliers
outliers = df[(df['Value'] < lower_bound) | (df['Value'] > upper_bound)]
print("\nIdentified Outliers:")
print(outliers)
# Output:
#    Value
# 8    100
# 9    200

# ---------------------------------------------------

# Removing Outliers
df_no_outliers = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]
print("\nDataFrame with Outliers Removed:")
print(df_no_outliers)
# Output:
#    Value
# 0     10
# 1     12
# 2     14
# 3     16
# 4     18
# 5     20
# 6     22
# 7     24

# ---------------------------------------------------

# 3. Handling Extreme Values (Capping)
data = {
    'Value': [10, 12, 14, 16, 18, 20, 22, 24, 1000, 2000]  # 1000 and 2000 are extreme values
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame with Extreme Values:")
print(df)
# Output:
#    Value
# 0     10
# 1     12
# 2     14
# 3     16
# 4     18
# 5     20
# 6     22
# 7     24
# 8   1000
# 9   2000

# ---------------------------------------------------

# Capping extreme values (winsorizing)
cap_value = df['Value'].quantile(0.95)  # Capping at the 95th percentile

df_capped = df.copy()
df_capped['Value'] = df_capped['Value'].clip(upper=cap_value)
print("\nDataFrame with Extreme Values Capped:")
print(df_capped)
# Output:
#    Value
# 0     10
# 1     12
# 2     14
# 3     16
# 4     18
# 5     20
# 6     22
# 7     24
# 8     24
# 9     24
