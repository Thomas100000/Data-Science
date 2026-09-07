import matplotlib.pyplot as plt

# Read values from file
x = []
y = []
with open("data.txt") as f:
    for line in f:
        a, b = line.split()
        x.append(float(a))
        y.append(float(b))

# Plot line
plt.plot(x, y)

# Labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot")

plt.show()
