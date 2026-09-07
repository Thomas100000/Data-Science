import matplotlib.pyplot as plt

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars, autopct='%1.1f%%')
plt.title(" Pie Chart")
plt.show()