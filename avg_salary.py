import pandas as pd

details={ 'Name':['a','b','c','d','e'],
          'occupation':['Engineer','Farmer','Mason','Driver','Engineer'],
          'Salary':[10000,20000,30000,40000,50000] }

df = pd.DataFrame(details)
print(df.to_string())
occ_average_age = df.groupby('occupation')['Salary'].mean()
print("Average salary per occupation : ")
print(occ_average_age)