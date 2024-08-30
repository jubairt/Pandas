import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Tom', 'Lucy'],
    'Age': [28, 34, 29, 31],
    'Salary': [50000, 60000, 55000, 70000]
}

df = pd.DataFrame(data)

def standardize(value):
    mean=df['Age'].mean()
    std=df['Age'].std()
    return (value-mean)/std
    

df['Age_ std']=df['Age'].transform(standardize)
print(df)