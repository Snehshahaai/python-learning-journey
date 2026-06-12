import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 90, 75, 95]
plt.pie(marks,labels=subjects,autopct="%1.1f%%")
plt.title("Subject Marks Distribution")

plt.show()