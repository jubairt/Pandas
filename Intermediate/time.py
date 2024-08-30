# DateTime objects in pandas: pd.to_datetime().

import pandas as pd

# Creating a DataFrame with date information as strings
data = {
    'Date': ['2024-01-01', '2024-02-15', '2024-03-20', '2024-04-10'],
    'Value': [100, 200, 300, 400]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Output:
# Original DataFrame:
#          Date  Value
# 0  2024-01-01    100
# 1  2024-02-15    200
# 2  2024-03-20    300
# 3  2024-04-10    400

# ---------------------------------------------------

# Converting the 'Date' column to DateTime objects using pd.to_datetime()
df['Date'] = pd.to_datetime(df['Date'])
print("\nDataFrame with 'Date' converted to DateTime:")
print(df)
# Output:
# DataFrame with 'Date' converted to DateTime:
#         Date  Value
# 0 2024-01-01    100
# 1 2024-02-15    200
# 2 2024-03-20    300
# 3 2024-04-10    400

# ---------------------------------------------------

# Converting a single date string to DateTime object
single_date = pd.to_datetime('2024-05-25')
print("\nSingle DateTime object from a string:")
print(single_date)
# Output:
# Single DateTime object from a string:
# 2024-05-25 00:00:00

# ---------------------------------------------------

# Converting a list of date strings to DateTime objects
date_list = ['2024-06-30', '2024-07-15', '2024-08-01']
date_series = pd.to_datetime(date_list)
print("\nDateTime Series from a list of date strings:")
print(date_series)
# Output:
# DateTime Series from a list of date strings:
# DatetimeIndex(['2024-06-30', '2024-07-15', '2024-08-01'], dtype='datetime64[ns]', freq=None)

# =================================================================================================

# Indexing by DateTime and resampling data with .resample().

import pandas as pd

# Creating a sample DataFrame with DateTime index
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Value': [10, 20, 15, 30, 25, 40, 35, 50, 45, 60]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)
print("Original DataFrame with DateTime Index:")
print(df)
# Output:
# Original DataFrame with DateTime Index:
#             Value
# Date             
# 2024-01-01     10
# 2024-01-02     20
# 2024-01-03     15
# 2024-01-04     30
# 2024-01-05     25
# 2024-01-06     40
# 2024-01-07     35
# 2024-01-08     50
# 2024-01-09     45
# 2024-01-10     60

# ---------------------------------------------------

# Resampling data to a weekly frequency and calculating the sum of 'Value'
df_resampled_weekly = df.resample('W').sum()
print("\nDataFrame Resampled to Weekly Frequency (Sum):")
print(df_resampled_weekly)
# Output:
# DataFrame Resampled to Weekly Frequency (Sum):
#             Value
# Date             
# 2024-01-07    120
# 2024-01-14    105

# ---------------------------------------------------

# Resampling data to a monthly frequency and calculating the mean of 'Value'
df_resampled_monthly = df.resample('M').mean()
print("\nDataFrame Resampled to Monthly Frequency (Mean):")
print(df_resampled_monthly)
# Output:
# DataFrame Resampled to Monthly Frequency (Mean):
#             Value
# Date             
# 2024-01-31    30.0

# ---------------------------------------------------

# Resampling data to a daily frequency with forward fill method
df_resampled_daily_ffill = df.resample('D').ffill()
print("\nDataFrame Resampled to Daily Frequency (Forward Fill):")
print(df_resampled_daily_ffill)
# Output:
# DataFrame Resampled to Daily Frequency (Forward Fill):
#             Value
# Date             
# 2024-01-01    10
# 2024-01-02    20
# 2024-01-03    15
# 2024-01-04    30
# 2024-01-05    25
# 2024-01-06    40
# 2024-01-07    35
# 2024-01-08    50
# 2024-01-09    45
# 2024-01-10    60

# ===========================================================================


# Rolling windows with .rolling() and cumulative operations.

import pandas as pd

# Creating a sample DataFrame
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Value': [10, 20, 15, 30, 25, 40, 35, 50, 45, 60]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)
print("Original DataFrame:")
print(df)
# Output:
# Original DataFrame:
#             Value
# Date             
# 2024-01-01     10
# 2024-01-02     20
# 2024-01-03     15
# 2024-01-04     30
# 2024-01-05     25
# 2024-01-06     40
# 2024-01-07     35
# 2024-01-08     50
# 2024-01-09     45
# 2024-01-10     60

# ---------------------------------------------------

# Rolling window: Calculate the rolling mean with a window size of 3
df['Rolling_Mean'] = df['Value'].rolling(window=3).mean()
print("\nRolling Mean with a Window Size of 3:")
print(df)
# Output:
# Rolling Mean with a Window Size of 3:
#             Value  Rolling_Mean
# Date                             
# 2024-01-01     10           NaN
# 2024-01-02     20           NaN
# 2024-01-03     15          15.0
# 2024-01-04     30          21.67
# 2024-01-05     25          23.33
# 2024-01-06     40          31.67
# 2024-01-07     35          33.33
# 2024-01-08     50          41.67
# 2024-01-09     45          43.33
# 2024-01-10     60          51.67

# ---------------------------------------------------

# Rolling window: Calculate the rolling sum with a window size of 3
df['Rolling_Sum'] = df['Value'].rolling(window=3).sum()
print("\nRolling Sum with a Window Size of 3:")
print(df)
# Output:
# Rolling Sum with a Window Size of 3:
#             Value  Rolling_Mean  Rolling_Sum
# Date                                       
# 2024-01-01     10           NaN          NaN
# 2024-01-02     20           NaN          NaN
# 2024-01-03     15          15.0         45.0
# 2024-01-04     30          21.67        65.0
# 2024-01-05     25          23.33        70.0
# 2024-01-06     40          31.67        90.0
# 2024-01-07     35          33.33       105.0
# 2024-01-08     50          41.67       125.0
# 2024-01-09     45          43.33       130.0
# 2024-01-10     60          51.67       150.0

# ---------------------------------------------------

# Cumulative operations: Calculate the cumulative sum
df['Cumulative_Sum'] = df['Value'].cumsum()
print("\nCumulative Sum:")
print(df)
# Output:
# Cumulative Sum:
#             Value  Rolling_Mean  Rolling_Sum  Cumulative_Sum
# Date                                                      
# 2024-01-01     10           NaN          NaN              10
# 2024-01-02     20           NaN          NaN              30
# 2024-01-03     15          15.0         45.0              45
# 2024-01-04     30          21.67        65.0              75
# 2024-01-05     25          23.33        70.0             100
# 2024-01-06     40          31.67        90.0             140
# 2024-01-07     35          33.33       105.0             175
# 2024-01-08     50          41.67       125.0             225
# 2024-01-09     45          43.33       130.0             270
# 2024-01-10     60          51.67       150.0             330

# ====================================================================================

# Time series shifting and lagging data.


import pandas as pd

# Creating a sample DataFrame with time series data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Value': [10, 20, 15, 30, 25, 40, 35, 50, 45, 60]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)
print("Original DataFrame:")
print(df)
# Output:
# Original DataFrame:
#             Value
# Date             
# 2024-01-01     10
# 2024-01-02     20
# 2024-01-03     15
# 2024-01-04     30
# 2024-01-05     25
# 2024-01-06     40
# 2024-01-07     35
# 2024-01-08     50
# 2024-01-09     45
# 2024-01-10     60

# ---------------------------------------------------

# Shifting data: Shift values down by 1 period
df['Shifted_Down'] = df['Value'].shift(1)
print("\nDataFrame with Shifted Down Values (Lagging by 1 period):")
print(df)
# Output:
# DataFrame with Shifted Down Values (Lagging by 1 period):
#             Value  Shifted_Down
# Date                             
# 2024-01-01     10           NaN
# 2024-01-02     20          10.0
# 2024-01-03     15          20.0
# 2024-01-04     30          15.0
# 2024-01-05     25          30.0
# 2024-01-06     40          25.0
# 2024-01-07     35          40.0
# 2024-01-08     50          35.0
# 2024-01-09     45          50.0
# 2024-01-10     60          45.0

# ---------------------------------------------------

# Lagging data: Shift values up by 1 period
df['Shifted_Up'] = df['Value'].shift(-1)
print("\nDataFrame with Shifted Up Values (Leading by 1 period):")
print(df)
# Output:
# DataFrame with Shifted Up Values (Leading by 1 period):
#             Value  Shifted_Down  Shifted_Up
# Date                                    
# 2024-01-01     10           NaN         20.0
# 2024-01-02     20          10.0         15.0
# 2024-01-03     15          20.0         30.0
# 2024-01-04     30          15.0         25.0
# 2024-01-05     25          30.0         40.0
# 2024-01-06     40          25.0         35.0
# 2024-01-07     35          40.0         50.0
# 2024-01-08     50          35.0         45.0
# 2024-01-09     45          50.0         60.0
# 2024-01-10     60          45.0          NaN

# ---------------------------------------------------

# Shifting data by more than one period
df['Shifted_Down_2'] = df['Value'].shift(2)
print("\nDataFrame with Shifted Down Values by 2 Periods:")
print(df)
# Output:
# DataFrame with Shifted Down Values by 2 Periods:
#             Value  Shifted_Down  Shifted_Up  Shifted_Down_2
# Date                                                       
# 2024-01-01     10           NaN         20.0            NaN
# 2024-01-02     20          10.0         15.0           10.0
# 2024-01-03     15          20.0         30.0           20.0
# 2024-01-04     30          15.0         25.0           15.0
# 2024-01-05     25          30.0         40.0           30.0
# 2024-01-06     40          25.0         35.0           25.0
# 2024-01-07     35          40.0         50.0           40.0
# 2024-01-08     50          35.0         45.0           35.0
# 2024-01-09     45          50.0         60.0           50.0
# 2024-01-10     60          45.0          NaN            45.0

# ---------------------------------------------------

# Lagging data by more than one period
df['Shifted_Up_2'] = df['Value'].shift(-2)
print("\nDataFrame with Shifted Up Values by 2 Periods:")
print(df)
# Output:
# DataFrame with Shifted Up Values by 2 Periods:
#             Value  Shifted_Down  Shifted_Up  Shifted_Down_2  Shifted_Up_2
# Date                                                                        
# 2024-01-01     10           NaN         20.0            NaN           15.0
# 2024-01-02     20          10.0         15.0           10.0           30.0
# 2024-01-03     15          20.0         30.0           20.0           25.0
# 2024-01-04     30          15.0         25.0           15.0           40.0
# 2024-01-05     25          30.0         40.0           30.0           35.0
# 2024-01-06     40          25.0         35.0           25.0           50.0
# 2024-01-07     35          40.0         50.0           40.0           45.0
# 2024-01-08     50          35.0         45.0           35.0           60.0
# 2024-01-09     45          50.0         60.0           50.0            NaN
# 2024-01-10     60          45.0          NaN           45.0            NaN

# ============================================================================================