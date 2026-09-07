import numpy as np

arr = np.array([10, 20, 30, 40, 50])

np.savetxt("array_data.txt", arr)

print("Array saved to array_data.txt")

loaded_arr = np.loadtxt("array_data.txt")

print("Loaded array:", loaded_arr)
