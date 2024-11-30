import pandas as pd

# Creating a sample DataFrame
data = {
    'Team': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Points': [10, 15, 10, 20, 25, 30, 35, 40],
    'Age': [23, 25, 24, 30, 28, 22, 21, 29]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Grouping by 'Team' and calculating the mean of each group
grouped_mean = df.groupby('Team').mean()
print("\nGrouped by 'Team' with mean aggregation:")
print(grouped_mean)
# Output:
#         Points   Age
# Team                
# A       21.25  24.25
# B       25.00  26.25

# ---------------------------------------------------
# Grouping by 'Team' and calculating the sum of each group
grouped_sum = df.groupby('Team').sum()
print("\nGrouped by 'Team' with sum aggregation:")
print(grouped_sum)
# Output:
#       Points  Age
# Team              
# A         85    97
# B        100   105

# ---------------------------------------------------
# Grouping by 'Team' and counting the number of occurrences in each group
grouped_count = df.groupby('Team').count()
print("\nGrouped by 'Team' with count aggregation:")
print(grouped_count)
# Output:
#       Points  Age
# Team              
# A          4     4
# B          4     4

# ---------------------------------------------------
# Grouping by 'Team' and calculating the minimum of each group
grouped_min = df.groupby('Team').min()
print("\nGrouped by 'Team' with min aggregation:")
print(grouped_min)
# Output:
#       Points  Age
# Team              
# A         10    21
# B         10    22

# ---------------------------------------------------
# Grouping by 'Team' and calculating the maximum of each group
grouped_max = df.groupby('Team').max()
print("\nGrouped by 'Team' with max aggregation:")
print(grouped_max)
# Output:
#       Points  Age
# Team              
# A         35    28
# B         40    30


# =====================================================================================

# .agg() for Multiple Aggregation Operations

import pandas as pd

# Creating a sample DataFrame
data = {
    'Team': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Points': [10, 15, 10, 20, 25, 30, 35, 40],
    'Age': [23, 25, 24, 30, 28, 22, 21, 29]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Grouping by 'Team' and applying multiple aggregation operations using .agg()
grouped_agg = df.groupby('Team').agg({
    'Points': ['mean', 'sum', 'max'],
    'Age': ['min', 'max']
})
print("\nGrouped by 'Team' with multiple aggregation functions using .agg():")
print(grouped_agg)
# Output:
#       Points               Age     
#         mean sum max  min max
# Team                          
# A       21.25  85  35   21  28
# B       25.00 100  40   22  30
