
import pandas as pd

details = {
    'cname' : ['a','b','c','d'],
    'profit' : [24,25,0,-27],
}

df = pd.DataFrame(details)
df['is_profitable'] = df['profit'] > 0
print(df)
