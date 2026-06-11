import numpy as np
marks = np.array([
    [85, 78, 92],
    [67, 88, 75],
    [90, 91, 89],
    [45, 55, 60],
    [72, 70, 68]
])
print("Total Student  Marks: ",np.sum(marks, axis=1))
average = np.average(marks,axis=1)
print("Average Marks of All Student: ",average)
print("Highest mark in the class: ",np.max(marks))
print("Lowest mark in the class: ",np.min(marks))
print("Students whose average is above 80: ",average[average>80])
print("Add 5 grace marks to every score: ",marks + 5)
print("Subject-wise average marks: ",np.average(marks,axis=0))
