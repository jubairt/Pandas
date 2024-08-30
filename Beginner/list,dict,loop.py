import pandas as pd

# Creating a list
students = ['John', 'Alice', 'Bob', 'Eve']
scores = [85, 92, 78, 88]

print(students)
# Output: ['John', 'Alice', 'Bob', 'Eve']

print(scores)
# Output: [85, 92, 78, 88]


# Creating a DataFrame from lists
data = {
    'Name': students,
    'Score': scores
}
df = pd.DataFrame(data)

print(df)
# Output:
#     Name  Score
# 0   John     85
# 1  Alice     92
# 2    Bob     78
# 3    Eve     88

# ---------------------------------------------------------------------------------------

# Creating a dictionary
student_info = {
    'John': 85,
    'Alice': 92,
    'Bob': 78,
    'Eve': 88
}

print(student_info)
# Output: {'John': 85, 'Alice': 92, 'Bob': 78, 'Eve': 88}

# Creating a DataFrame from a dictionary
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve'],
    'Score': [85, 92, 78, 88]
}
df = pd.DataFrame(data)

print(df)
# Output:
#     Name  Score
# 0   John     85
# 1  Alice     92
# 2    Bob     78
# 3    Eve     88

# -----------------------------------------------------------------------------------------

# Using a for loop to print each student and their score
for student, score in student_info.items():
    print(f"{student}: {score}")
    
# Output:
# John: 85
# Alice: 92
# Bob: 78
# Eve: 88

# Using a for loop to iterate over DataFrame rows
for index, row in df.iterrows():
    print(f"Student: {row['Name']}, Score: {row['Score']}")
    
# Output:
# Student: John, Score: 85
# Student: Alice, Score: 92
# Student: Bob, Score: 78
# Student: Eve, Score: 88
