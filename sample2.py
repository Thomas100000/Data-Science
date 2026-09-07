import pandas as pd
s= pd.Series([10,20,30,40])
print(s)

data={
    "Name": ["Alice","Bob","Charlie"],
    "Age":[20,22,21],
    "Marks":[85,90,88]
}
df = pd.DataFrame(data)
print(df)