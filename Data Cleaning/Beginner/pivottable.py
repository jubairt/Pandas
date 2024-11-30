import pandas as pd

# Sample data - Sales data for different products across different regions
data = {
    'Region': ['North', 'North', 'East', 'East', 'South', 'South', 'West', 'West', 'North', 'East'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture', 'Furniture', 'Electronics'],
    'Sales': [200, 300, 150, 400, 100, 250, 450, 350, 500, 600],
    'Profit': [20, 30, 15, 40, 10, 25, 45, 35, 50, 60]
}

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)
# Output:
#   Region    Category  Sales  Profit
# 0  North  Electronics    200      20
# 1  North   Furniture    300      30
# 2   East  Electronics    150      15
# 3   East   Furniture    400      40
# 4  South  Electronics    100      10
# 5  South   Furniture    250      25
# 6   West  Electronics    450      45
# 7   West   Furniture    350      35
# 8  North   Furniture    500      50
# 9   East  Electronics    600      60

# Pivot table summarizing total sales by region
pivot_table_sales = pd.pivot_table(df, values='Sales', index='Region', aggfunc='sum')
print(pivot_table_sales)
# Output:
#         Sales
# Region         
# East      1150
# North     1000
# South      350
# West       800

# Pivot table with multiple aggregation functions
pivot_table_summary = pd.pivot_table(df, values='Sales', index='Region', aggfunc=['sum', 'mean', 'count'])
print(pivot_table_summary)
# Output:
#          sum   mean  count
# Region                      
# East     1150  383.3      3
# North    1000  333.3      3
# South     350  175.0      2
# West      800  400.0      2

# Pivot table summarizing total sales by region and category
pivot_table_region_category = pd.pivot_table(df, values='Sales', index='Region', columns='Category', aggfunc='sum')
print(pivot_table_region_category)
# Output:
# Category  Electronics  Furniture
# Region                          
# East              750        400
# North             200        800
# South             100        250
# West              450        350

# Pivot table summarizing both Sales and Profit by region and category
pivot_table_sales_profit = pd.pivot_table(df, values=['Sales', 'Profit'], index='Region', columns='Category', aggfunc='sum')
print(pivot_table_sales_profit)
# Output:
#          Sales                  Profit             
# Category Electronics Furniture Electronics Furniture
# Region                                               
# East           750      400         75         40
# North          200      800         20         80
# South          100      250         10         25
# West           450      350         45         35

# Different aggregation functions for different columns
pivot_table_custom = pd.pivot_table(df, values=['Sales', 'Profit'], index='Region', aggfunc={'Sales': 'sum', 'Profit': 'mean'})
print(pivot_table_custom)
# Output:
#         Sales  Profit
# Region                
# East      1150    25.0
# North     1000    50.0
# South      350    17.5
# West       800    40.0

# Pivot table with margins (totals) and fill_value for NaNs
pivot_table_advanced = pd.pivot_table(df, values='Sales', index='Region', columns='Category', aggfunc='sum', margins=True, fill_value=0)
print(pivot_table_advanced)
# Output:
# Category  Electronics  Furniture   All
# Region                                
# East              750        400  1150
# North             200        800  1000
# South             100        250   350
# West              450        350   800
# All              1500       1800  3300
