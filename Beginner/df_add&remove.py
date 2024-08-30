# 1. Adding Columns
import pandas as pd

# Creating a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Score': [85, 90, 75]
}
df = pd.DataFrame(data)

# Adding a new column with scalar values
df['Passed'] = True

print(df)
# Output:
#       Name  Age  Score  Passed
# 0    Alice   25     85    True
# 1      Bob   30     90    True
# 2  Charlie   22     75    True

# ---------------------------------------------------

# Adding a new column with a list
df['Country'] = ['USA', 'Canada', 'UK']

print(df)
# Output:
#       Name  Age  Score  Passed Country
# 0    Alice   25     85    True     USA
# 1      Bob   30     90    True  Canada
# 2  Charlie   22     75    True      UK

# ---------------------------------------------------

# Adding a new column by performing an operation on existing columns
df['Age Group'] = ['Adult' if age >= 25 else 'Youth' for age in df['Age']]

print(df)
# Output:
#       Name  Age  Score  Passed Country Age Group
# 0    Alice   25     85    True     USA     Adult
# 1      Bob   30     90    True  Canada     Adult
# 2  Charlie   22     75    True      UK     Youth

# -----------------------------------------------------------------------------

# 2. Removing Columns
# Removing a single column
df = df.drop('Passed', axis=1)

# The axis parameter in the drop() function specifies whether you're dropping rows or columns. The key distinction is:

# axis=0: This refers to rows.
# axis=1: This refers to columns.

print(df)
# Output:
#       Name  Age  Score Country Age Group
# 0    Alice   25     85     USA     Adult
# 1      Bob   30     90  Canada     Adult
# 2  Charlie   22     75      UK     Youth

# ---------------------------------------------------

# Removing multiple columns
df = df.drop(['Country', 'Age Group'], axis=1)

print(df)
# Output:
#       Name  Age  Score
# 0    Alice   25     85
# 1      Bob   30     90
# 2  Charlie   22     75


# -----------------------------------------------------------------------------
#  this is recommended in new versions
import pandas as pd

# Adding rows using concat (instead of append)
new_row = pd.DataFrame({'Name': ['David'], 'Age': [28], 'Score': [88]})
df = pd.concat([df, new_row], ignore_index=True)


# -----------------------------------------------------------------------------

# 3. Adding Rows
# Adding a new row
new_row = {'Name': 'David', 'Age': 28, 'Score': 88}
df = df.append(new_row, ignore_index=True)

print(df)
# Output:
#       Name  Age  Score
# 0    Alice   25     85
# 1      Bob   30     90
# 2  Charlie   22     75
# 3    David   28     88


# -----------------------------------------------------------------------------

# 4. Removing Rows
# Removing a row by index
df = df.drop(2)

print(df)
# Output:
#      Name  Age  Score
# 0   Alice   25     85
# 1     Bob   30     90
# 3   David   28     88

# ---------------------------------------------------

# Removing multiple rows by index
df = df.drop([0, 3])

print(df)
# Output:
#    Name  Age  Score
# 1   Bob   30     90



# -----------------------------------------------------------------------------