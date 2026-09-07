import pandas as pd
import numpy as np
occ={'Set_of_occupations':['A',np.nan,'B',np.nan,'D','E']}
df=pd.DataFrame(occ,columns=['Set_of_occupations'])
df['Set_of_occupations']=df['Set_of_occupations'].fillna(0)
print(df)