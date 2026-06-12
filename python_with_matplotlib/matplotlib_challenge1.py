import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [100, 150, 200, 180, 250]
plt.plot(days,sales)
plt.title("Daily Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()