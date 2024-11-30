outliers=df[(df['Values']<lower_bound)|(df['Values']>upper_bound)]
# print(outliers)