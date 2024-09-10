import pandas as pd

import pandas as pd

# Creating a sample Employee Performance DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Tom', 'Lucy', 'Mark', 'Eve', 'Chris', 'David'],
    'Department': ['Sales', 'HR', 'Sales', 'IT', 'IT', 'HR', 'Sales', 'Finance', 'Finance', 'Sales'],
    'Age': [29, 34, 26, 41, 28, 38, 31, 45, 33, 30],
    'Salary': [50000, 60000, 52000, 72000, 55000, 64000, 53000, 75000, 58000, 51000],
    'PerformanceScore': [85, 90, 88, 92, 79, 85, 83, 91, 86, 82],
    'YearsAtCompany': [3, 5, 2, 10, 3, 7, 4, 11, 5, 2]
}

df = pd.DataFrame(data)

# Find the employee with the highest salary

highest_salary = df[df['Salary'] == df['Salary'].max()]

print(highest_salary)


# ----------------------------------------------------------------

# Calculate average salary per department
average_salary = df.groupby('Department')['Salary'].mean()

# Find the department with the highest average salary
# !check
highest_avg_salary_department = average_salary.idxmax()

print("Average Salary per Department:\n", average_salary)
print("\nDepartment with Highest Average Salary:", highest_avg_salary_department)

# ---------------------------------------------------------------------------------------

# Add 10% bonus to each salary
df['SalaryBonus'] = df['Salary'] * 1.10

print(df[['Name', 'Salary', 'SalaryBonus']])


# ---------------------------------------------------------------------------------------

# Filter employees in Sales department with PerformanceScore > 85
# !check
high_performance_sales = df[(df['Department'] == 'Sales') & (df['PerformanceScore'] > 85)]

print(high_performance_sales)


# ---------------------------------------------------------------------------------------

# Calculate cumulative sum of YearsAtCompany
df['Cumulative_YearsAtCompany'] = df['YearsAtCompany'].cumsum()

print(df[['Name', 'YearsAtCompany', 'Cumulative_YearsAtCompany']])


# ---------------------------------------------------------------------------------------

# Additional employee details
location_data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Location': ['New York', 'Chicago', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'New York']
}

location_df = pd.DataFrame(location_data)

# Merging location data with employee data

merged_df = pd.merge(df, location_df, on='EmployeeID')

print(merged_df)


# ---------------------------------------------------------------------------------------

# Create a pivot table with average PerformanceScore per Department

pivot = df.pivot_table(values='PerformanceScore', index='Department', aggfunc='mean')

print(pivot)


# ---------------------------------------------------------------------------------------

# 1. What is the average salary in the IT department?
it_avg_salary = df[df['Department'] == 'IT']['Salary'].mean()
print(it_avg_salary)

# ---------------------------------------------------------------------------------------

# 2. How many employees have worked at the company for more than 5 years?

employees_more_than_5_years = df[df['YearsAtCompany'] > 5].shape[0]
print(employees_more_than_5_years)


# ---------------------------------------------------------------------------------------

# 3. What is the name of the employee with the highest performance score?
top_performer = df[df['PerformanceScore'] == df['PerformanceScore'].max()]['Name'].iloc[0]
print(top_performer)


# ---------------------------------------------------------------------------------------

# 6. What is the total salary expense for the HR department?
hr_salary_expense = df[df['Department'] == 'HR']['Salary'].sum()
print(hr_salary_expense)


# ---------------------------------------------------------------------------------------

# 7. Find the employee with the lowest salary. What is their name and department?
lowest_salary_employee = df[df['Salary'] == df['Salary'].min()][['Name', 'Department']].iloc[0]
print(lowest_salary_employee)


# ---------------------------------------------------------------------------------------

# 8. What is the median salary of all employees?
median_salary = df['Salary'].median()
print(median_salary)


# ---------------------------------------------------------------------------------------

# 9. How many departments have an average salary above $60,000?
# !check
high_salary_departments = df.groupby('Department')['Salary'].mean()
departments_above_60k = high_salary_departments[high_salary_departments > 60000].count()
print(departments_above_60k)


# ---------------------------------------------------------------------------------------

# 10. Which employee has the most years at the company and what is their performance score?
most_years_employee = df[df['YearsAtCompany'] == df['YearsAtCompany'].max()][['Name', 'PerformanceScore']].iloc[0]
print(most_years_employee)

# ---------------------------------------------------------------------------------------

# 2. What is the average performance score for employees under 30?
avg_perf_under_30 = df[df['Age'] < 30]['PerformanceScore'].mean()
print(avg_perf_under_30)


# ---------------------------------------------------------------------------------------
# !check
# 3. How many employees are in each department?
employees_per_department = df['Department'].value_counts()
print(employees_per_department)


# ---------------------------------------------------------------------------------------

# 4. What is the maximum salary in each department?
max_salary_per_department = df.groupby('Department')['Salary'].max()
print(max_salary_per_department)


# ---------------------------------------------------------------------------------------
# 7. List employees who have both a performance score above 85 and have been at the company for more than 5 years.
high_empl=(df['PerformanceScore']>85) & (df['YearsAtCompany']>5)
print(df[high_empl]['Name'])

# ---------------------------------------------------------------------------------------


# 8. What is the median age of employees in the Sales department?
median_age_sales = df[df['Department'] == 'Sales']['Age'].median()
print(median_age_sales)

# ---------------------------------------------------------------------------------------

# 9. How many departments have an average salary above $60,000?
high_salary_departments = df.groupby('Department')['Salary'].mean()
departments_above_60k = high_salary_departments[high_salary_departments > 60000].count()
print(departments_above_60k)


# ---------------------------------------------------------------------------------------

# 10. Which employee has the most years at the company and what is their performance score?
most_years_employee = df[df['YearsAtCompany'] == df['YearsAtCompany'].max()][['Name', 'PerformanceScore']].iloc[0]
print(most_years_employee)


# ---------------------------------------------------------------------------------------

# 1. How many employees are older than 30?
employees_older_than_30 = df[df['Age'] > 30].shape[0]
print(employees_older_than_30)

# ---------------------------------------------------------------------------------------

# 6. What is the total number of employees in the dataset?
total_employees = df.shape[0]
print(total_employees)


# ---------------------------------------------------------------------------------------

# 9. Which employee has the second highest salary?
second_highest_salary = df.nlargest(2, 'Salary')['Name'].iloc[-1]
print(second_highest_salary)

# ---------------------------------------------------------------------------------------

# 16. Find the top 3 employees by performance score.
top_3_performers = df.nlargest(3, 'PerformanceScore')[['Name', 'PerformanceScore']]
print(top_3_performers)


# ---------------------------------------------------------------------------------------

# 16. Find the top 3 employees by performance score.

# Sort the DataFrame by 'PerformanceScore' in descending order
emplo = df.sort_values(by='PerformanceScore', ascending=False)

# Selecting the first 3 rows (top 3 employees by performance score) and columns by position
top_3 = emplo.iloc[:3, [0, 1]]  # First 3 rows and columns by position (0 = Name, 1 = PerformanceScore)

# ---------------------------------------------------------------------------------------

# 17. What is the name of the employee with the third lowest salary?
third_lowest_salary = df.nsmallest(3, 'Salary')['Name'].iloc[-1]
print(third_lowest_salary)

# ---------------------------------------------------------------------------------------

# 20. Get the names of employees whose performance score is below the average.
below_avg_performance = df[df['PerformanceScore'] < df['PerformanceScore'].mean()]['Name']
print(below_avg_performance)

# ---------------------------------------------------------------------------------------

# 21. Which employee has the closest salary to the average salary?
# !check
avg_salary_closest = df.iloc[(df['Salary'] - df['Salary'].mean()).abs().argsort()[:1]]['Name'].iloc[0]
print(avg_salary_closest)


# ---------------------------------------------------------------------------------------

# 21. Which employee has the closest salary to the average salary?
# !check
# Calculate the average salary
average_salary = df['Salary'].mean()

# Find the employee with the closest salary to the average salary
df['Salary_Difference'] = abs(df['Salary'] - average_salary)
closest_salary_emp = df.loc[df['Salary_Difference'].idxmin()]

# Print the employee with the closest salary to the average salary
print(closest_salary_emp[['Name', 'Salary']])

# ---------------------------------------------------------------------------------------
# !check
# 22. How many employees have a salary between 50,000 and 60,000?
how=df['Salary'].between(50000,60000).sum()
print(how)

# ---------------------------------------------------------------------------------------

# 22. How many employees have a salary between 50,000 and 60,000?
salary_range_employees = df[(df['Salary'] >= 50000) & (df['Salary'] <= 60000)].shape[0]
print(salary_range_employees)


# ---------------------------------------------------------------------------------------

# 23. Find the average number of years at the company for employees with a salary over 55,000.
avg_years_high_salary = df[df['Salary'] > 55000]['YearsAtCompany'].mean()
print(avg_years_high_salary)


# ---------------------------------------------------------------------------------------

# 29. Which employee has the highest salary-to-age ratio?
highest_salary_age_ratio = (df['Salary'] / df['Age']).idxmax()
employee_high_salary_age_ratio = df.loc[highest_salary_age_ratio, 'Name']
print(employee_high_salary_age_ratio)


# ---------------------------------------------------------------------------------------

# 30. Find the name of the employee who is closest to retirement (assuming 65 as retirement age).
# !check
closest_to_retirement = df.loc[(65 - df['Age']).idxmin()]['Name']
print(closest_to_retirement)

# ---------------------------------------------------------------------------------------

# 3. Determine the number of employees in each age group (e.g., 20-30, 31-40, 41-50).
bins = [20, 30, 40, 50]
labels = ['20-30', '31-40', '41-50']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
age_group_counts = df['Age_Group'].value_counts()
print("Number of Employees in Each Age Group:")
print(age_group_counts)


# ---------------------------------------------------------------------------------------

# 4. Find the highest salary for each performance score group and sort the results by performance score.
highest_salary_by_performance = df.groupby('PerformanceScore')['Salary'].max().sort_index()
print("Highest Salary by Performance Score (Sorted):")
print(highest_salary_by_performance)


# ---------------------------------------------------------------------------------------
# ! check
# 7. Find the median salary of employees for each unique age.
median_salary_by_age = df.groupby('Age')['Salary'].median()
print("Median Salary by Age:")
print(median_salary_by_age)

# ==============================================================================================

# Based on series concepts

# 2. Create a Series from a dictionary where the keys are 'EmployeeID' and the values are 'Salary'.
salary_dict = df.set_index('EmployeeID')['Salary'].to_dict()
salary_series = pd.Series(salary_dict)
print("Series from dictionary (EmployeeID as index, Salary as values):")
print(salary_series)

# ---------------------------------------------------------------------------------------

# 18. Convert the 'Age' column to a Series and replace all ages below 30 with 30.
ser=df['Age'].apply(lambda age:30 if age<30 else age)
print(ser)
# --------
# 18. Convert the 'Age' column to a Series and replace all ages below 30 with 30.
# !check
age_series = df['Age']
age_series_updated = age_series.apply(lambda x: max(x, 30))
print("Updated Age Series (Ages Below 30 Set to 30):")
print(age_series_updated)
# ============================================================================
# 2. Remove the 'Bonus' column from the DataFrame.
# !check
df=pd.DataFrame(data)
df['hi']=500
print(df)
df=df.drop(columns='hi')
print(df)


# ---------------------------------------------------------------------------------------

# 3. Add a new row to the DataFrame with data for a new employee.
# !check
new_employee = pd.DataFrame({
    'EmployeeID': [111],
    'Name': ['New Employee'],
    'Department': ['Marketing'],
    'Age': [27],
    'Salary': [58000],
    'PerformanceScore': [87],
    'YearsAtCompany': [1]
})
df = pd.concat([df, new_employee], ignore_index=True)
print("DataFrame with New Employee Added:")
print(df)


# ---------------------------------------------------------------------------------------
# !check
# Remove the row with EmployeeID 101
df = df[df['EmployeeID'] != 101]

# Alternatively, using drop() with index
df = df.set_index('EmployeeID').drop(101).reset_index()

# ---------------------------------------------------------------------------------------

# 12. Use the map() function to replace department names with their abbreviations.
# !check
department_abbr = {
    'Sales': 'SL',
    'HR': 'HR',
    'IT': 'IT',
    'Finance': 'FN',
    'Marketing': 'MK'
}
df['Department_Abbr'] = df['Department'].map(department_abbr)
print("DataFrame with 'Department_Abbr' Column Added:")
print(df[['Department', 'Department_Abbr']])


# ---------------------------------------------------------------------------------------

# 14. Sort the DataFrame by 'Age' and then by 'Salary' in ascending order.
df_sorted_age_salary = df.sort_values(by=['Age', 'Salary'])
print("DataFrame Sorted by Age and Salary (Ascending):")
print(df_sorted_age_salary[['Name', 'Age', 'Salary']])

# ==========================================================================================
# Strings
# !check
# 5. Filter employees whose names start with the letter 'J'.
names_start_with_J = df[df['Name'].str.startswith('J')]
print(names_start_with_J)

# ---------------------------------------------------------------------------------------

# 6. Filter employees whose names contain 'o'.
names_contain_o = df[df['Name'].str.contains('o', case=False)]
print(names_contain_o)

# ---------------------------------------------------------------------------------------
# 8. Change the 'Department' column's string values to lowercase.
df['Department'] = df['Department'].str.lower()
print(df)

# ---------------------------------------------------------------------------------------
# !check
# 11. Rename the 'Salary' column to 'AnnualSalary'.
df.rename(columns={'Salary': 'AnnualSalary'}, inplace=True)
print(df)

# ---------------------------------------------------------------------------------------
# 12. Rename the 'Age' column to 'Employee_Age' and 'PerformanceScore' to 'Perf_Score'.

change={
    'Age':'empl_age',
    'PerformanceScore':'per_score'
}
df.rename(columns=change,inplace=True)
print(df)

# ---------------------------------------------------------------------------------------
# !check
# 13. Rename all the columns to lowercase.
df.columns = df.columns.str.lower()
print(df)

# ---------------------------------------------------------------------------------------
# !check
# 15. Convert the 'Employee_Age' column to float type.
df['employee_age'] = df['employee_age'].astype(float)
print(df.dtypes)
# ====================================================================================
# Handling missing data
# 1. Identify which columns contain any missing values.
missing_columns = df.isna().any()
print(missing_columns)

# ---------------------------------------------------------------------------------------
# 2. Check the total number of missing values in the entire DataFrame.
total_missing = df.isna().sum().sum()
print(total_missing)

# ---------------------------------------------------------------------------------------
# 3. Check how many missing values are in each column.
missing_per_column = df.isna().sum()
print(missing_per_column)

# ---------------------------------------------------------------------------------------
# 5. Find rows where any data is missing.
rows_with_missing_data = df[df.isna().any(axis=1)]
print(rows_with_missing_data)


# ---------------------------------------------------------------------------------------
# !check
# 7. Use forward fill (`.fillna(method='ffill')`) to fill missing values in the 'Salary' column.
df['Salary'] = df['Salary'].fillna(method='ffill')
print(df)

# ---------------------------------------------------------------------------------------
# 9. Fill missing values in 'YearsAtCompany' with the column's mean.
df['YearsAtCompany'] = df['YearsAtCompany'].fillna(df['YearsAtCompany'].mean())
print(df)

# ---------------------------------------------------------------------------------------
# !check
# 12. Drop rows where any data is missing.
df_no_missing = df.dropna()
print(df_no_missing)

# ---------------------------------------------------------------------------------------
# 13. Drop rows where all data is missing (completely empty rows).
df_no_empty_rows = df.dropna(how='all')
print(df_no_empty_rows)

# ---------------------------------------------------------------------------------------
# 14. Drop rows where 'Salary' is missing.
df_no_missing_salary = df.dropna(subset=['Salary'])
print(df_no_missing_salary)

# ---------------------------------------------------------------------------------------
# 20. Fill missing values in 'Salary' by interpolating between available values.
df['Salary'] = df['Salary'].interpolate()
print(df)

# ---------------------------------------------------------------------------------------
# 6. For each department, get both the average salary and total years at the company.
salary_and_years_per_department = df.groupby('Department').agg({'Salary': 'mean', 'YearsAtCompany': 'sum'})
print(salary_and_years_per_department)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
