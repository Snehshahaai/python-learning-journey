import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 60, 65, 75, 85, 95]

plt.scatter(hours_studied,marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

