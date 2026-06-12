import matplotlib.pyplot as plt
students = ["Rahul", "Priya", "Amit", "Karan"]
marks = [85, 92, 78, 88]
plt.bar(students,marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()