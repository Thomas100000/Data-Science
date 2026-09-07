import numpy as np
ar=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ar)
print("\nsum")
print(np.sum(ar))

print("sum of columns")
print(np.sum(ar, axis=0))
print("\nsum of rows")
print(np.sum(ar, axis=1))