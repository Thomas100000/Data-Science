import numpy as np

nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)

new_arr=np.diag(nums)
print("New array:")
print(new_arr)
