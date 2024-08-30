# Handling String Data with .str Accessor
# The .str accessor allows you to perform various operations on string columns, such as:

# String Methods: .lower(), .upper(), .title(), .strip(), etc.
# Pattern Matching: .contains(), .startswith(), .endswith()
# String Splitting: .split(), .splitn()
# String Replacement: .replace()
# String Extraction: .extract(), .find()


import pandas as pd

# Creating a sample DataFrame with string data
data = {
    'Name': [' Alice', 'Bob Smith', 'charlie', 'David O\'Conner', 'Eve '],
    'Email': ['alice@example.com', 'bob.smith@example.com', 'charlie@example.com', 'david.oconner@example.com', 'eve@example.com']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ---------------------------------------------------

# 1. Converting to Lowercase

# Convert the 'Name' column to lowercase
df['Name_Lower'] = df['Name'].str.lower()

print("\nDataFrame with 'Name' in Lowercase:")
print(df)
# Output:
#            Name                Email          Name_Lower
# 0          Alice    alice@example.com                alice
# 1      Bob Smith  bob.smith@example.com            bob smith
# 2        charlie    charlie@example.com            charlie
# 3  David O'Conner  david.oconner@example.com  david o'conner
# 4            Eve       eve@example.com                eve

# ---------------------------------------------------

# 2. Stripping Whitespace

# Strip leading and trailing whitespace from the 'Name' column
df['Name_Trimmed'] = df['Name'].str.strip()

print("\nDataFrame with 'Name' Trimmed:")
print(df)
# Output:
#            Name                Email          Name_Lower Name_Trimmed
# 0          Alice    alice@example.com                alice        Alice
# 1      Bob Smith  bob.smith@example.com            bob smith    Bob Smith
# 2        charlie    charlie@example.com            charlie      charlie
# 3  David O'Conner  david.oconner@example.com  david o'conner  David O'Conner
# 4            Eve       eve@example.com                eve            Eve

# ---------------------------------------------------

# 3. Checking for Substrings

# Check if 'Email' contains 'example.com'
df['Contains_Example'] = df['Email'].str.contains('example.com')

print("\nDataFrame with Email Contains 'example.com':")
print(df)
# Output:
#            Name                Email          Name_Lower Name_Trimmed  Contains_Example
# 0          Alice    alice@example.com                alice        Alice              True
# 1      Bob Smith  bob.smith@example.com            bob smith    Bob Smith              True
# 2        charlie    charlie@example.com            charlie      charlie              True
# 3  David O'Conner  david.oconner@example.com  david o'conner  David O'Conner              True
# 4            Eve       eve@example.com                eve            Eve              True

# ---------------------------------------------------

# 4. Splitting Strings

# Split the 'Name' column into first and last names

# .split(' '): This part splits a string into separate parts using a space (' ') as the delimiter. When applied to a pandas Series, it splits each string element at every space by default.

# 1: This is the n parameter in the .split() method, which specifies the maximum number of splits. By using 1, you tell pandas to split the string only once at the first occurrence of a space. This ensures that you don't split on every space but only on the first space encountered in each string.

# expand=True: This parameter makes pandas return a DataFrame instead of a Series. When expand=True, pandas separates the results of the split into multiple columns (in this case, two columns), rather than returning a list in each cell.

df[['First_Name', 'Last_Name']] = df['Name_Trimmed'].str.split(' ', 1, expand=True)

print("\nDataFrame with 'Name' Split into First and Last Names:")
print(df)
# Output:
#            Name                Email          Name_Lower Name_Trimmed  Contains_Example First_Name  Last_Name
# 0          Alice    alice@example.com                alice        Alice              True     Alice        NaN
# 1      Bob Smith  bob.smith@example.com            bob smith    Bob Smith              True        Bob      Smith
# 2        charlie    charlie@example.com            charlie      charlie              True   charlie        NaN
# 3  David O'Conner  david.oconner@example.com  david o'conner  David O'Conner              True      David   O'Conner
# 4            Eve       eve@example.com                eve            Eve              True        Eve        NaN

# ---------------------------------------------------

# 5. Replacing Substrings

# Replace 'example.com' with 'sample.com' in the 'Email' column
df['Email_Replaced'] = df['Email'].str.replace('example.com', 'sample.com')

print("\nDataFrame with 'Email' Replaced:")
print(df)
# Output:
#            Name                Email          Name_Lower Name_Trimmed  Contains_Example  \
# 0          Alice    alice@example.com                alice        Alice              True   
# 1      Bob Smith  bob.smith@example.com            bob smith    Bob Smith              True   
# 2        charlie    charlie@example.com            charlie      charlie              True   
# 3  David O'Conner  david.oconner@example.com  david o'conner  David O'Conner              True   
# 4            Eve       eve@example.com                eve            Eve              True   

#                      Email_Replaced  
# 0          alice@sample.com  
# 1      bob.smith@sample.com  
# 2      charlie@sample.com  
# 3  david.oconner@sample.com  
# 4          eve@sample.com  
