import pandas as pd

# Data Frame
data={
    "student":["jubair","jasi","jabi"],
    "Mark":[87,54,34],
    "Rank":[1,2,3],
}

df=pd.DataFrame(data)
print(df)

# access datas by rows
df=pd.DataFrame(data, index=['rowA','rowB','rowC'])
print("\n",df.loc['rowA'])
print("\n",df.loc['rowA',"student"])
