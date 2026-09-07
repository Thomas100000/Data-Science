import matplotlib.pyplot as plt

figure, axis = plt.subplots(2,2)


x1 = [10,20,30]
y1 = [10,20,30]
axis[0, 0].plot(x1, y1)
axis[0, 0].set_title("Plot 1")

x2 = [10,10,10]
y2 = [30,40,50]
axis[0, 1].plot(x2, y2)
axis[0, 1].set_title("Plot 2")

x3 = [1, 2, 3]
y3 = [3, 2, 1]
axis[1, 0].plot(x3, y3)
axis[1, 0].set_title("Plot 3")

# Plot 4
x4 = [5, 6, 7]
y4 = [7, 6, 5]
axis[1, 1].plot(x4, y4)
axis[1, 1].set_title("Plot 4")
plt.show()