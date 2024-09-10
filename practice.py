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

new=df1.join(df2)
print(new)