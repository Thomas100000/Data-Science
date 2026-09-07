import pandas as pd
details={ 'Name':['a','b','c','d','e'],
         'Age':[19,22,23,24,25],
          }
df= pd.DataFrame(details)
print(df[:2])