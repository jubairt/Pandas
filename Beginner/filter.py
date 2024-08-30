import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [85, 90, 75, 60, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ---------------------------------------------------

# 1. Filtering Based on a Single Condition

# Define the condition
condition = df['Age'] > 30

# Apply the condition to filter rows
filtered_df = df[condition]

print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)
# Output:
#       Name  Age  Score
# 2  Charlie   35     75
# 3    David   40     60
# 4      Eve   45     95

# ---------------------------------------------------

# 2. Filtering Based on Multiple Conditions

# Define multiple conditions
condition = (df['Age'] > 30) & (df['Score'] > 70)

# Apply the condition to filter rows
filtered_df = df[condition]

print("\nFiltered DataFrame (Age > 30 and Score > 70):")
print(filtered_df)
# Output:
#       Name  Age  Score
# 2  Charlie   35     75
# 4      Eve   45     95

# ---------------------------------------------------

# 3. Filtering with `isin()` Method

# Define the condition using `isin()`
condition = df['Name'].isin(['Alice', 'Eve'])

# Apply the condition to filter rows
filtered_df = df[condition]

print("\nFiltered DataFrame (Name is 'Alice' or 'Eve'):")
print(filtered_df)
# Output:
#       Name  Age  Score
# 0    Alice   25     85
# 4      Eve   45     95

# ---------------------------------------------------

# 4. Filtering with `~` (NOT) Operator

# Define the condition using `~` for NOT
condition = ~(df['Age'] > 30)

# Apply the condition to filter rows
filtered_df = df[condition]

print("\nFiltered DataFrame (Age NOT > 30):")
print(filtered_df)
# Output:
#     Name  Age  Score
# 0  Alice   25     85
# 1    Bob   30     90
