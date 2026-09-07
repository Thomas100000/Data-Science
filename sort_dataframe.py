import pandas as pd
df=pd.DataFrame({'Name':[3,1,2],
'Mark':[89,88,87],
'Course':['BCA','MCA','IMCA']})
print(df.to_string())
print('Sorted values:')
order=df.sort_values(by=['Name','Mark'],ascending=[True,True])
print(order.to_string())
