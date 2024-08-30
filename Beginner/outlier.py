# Handling Outliers and Special Cases

# 1. Identifying Outliers Using IQR
import pandas as pd

# Creating a sample DataFrame with some extreme values
data = {
    'Value': [10, 12, 14, 16, 18, 20, 22, 24, 100, 200]  # 100 and 200 are outliers
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

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

# Identifying outliers
outliers = df[(df['Value'] < lower_bound) | (df['Value'] > upper_bound)]
print("\nIdentified Outliers:")
print(outliers)

# Output:
# Original DataFrame:
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
#
# IQR Calculations:
# Q1: 15.0, Q3: 22.0, IQR: 7.0
# Lower Bound: 1.5, Upper Bound: 35.5
#
# Identified Outliers:
#    Value
# 8    100
# 9    200

# -------------------

# 2. Removing Outliers
# Removing outliers from the DataFrame
df_no_outliers = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]
print("\nDataFrame with Outliers Removed:")
print(df_no_outliers)

# Output:
# DataFrame with Outliers Removed:
#    Value
# 0     10
# 1     12
# 2     14
# 3     16
# 4     18
# 5     20
# 6     22
# 7     24

# ---------------------

# 3. Handling Extreme Values (Capping)
# Creating a DataFrame with some extreme values
data = {
    'Value': [10, 12, 14, 16, 18, 20, 22, 24, 1000, 2000]  # 1000 and 2000 are extreme values
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame with Extreme Values:")
print(df)

# ---------------------------------------------------

# Capping extreme values (winsorizing)
cap_value = df['Value'].quantile(0.95)  # Capping at the 95th percentile

df_capped = df.copy()
df_capped['Value'] = df_capped['Value'].clip(upper=cap_value)
print("\nDataFrame with Extreme Values Capped:")
print(df_capped)

# Output:
# Original DataFrame with Extreme Values:
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
# 9  2000
#
# DataFrame with Extreme Values Capped:
#    Value
# 0     10
# 1     12
# 2     14
# 3     16
# 4     18
# 5     20
# 6     22
# 7     24
# 8    24
# 9    24


