import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Karan", "Neha"],
    "Age": [20, 19, 21, 22, 20],
    "Marks": [85, 92, 78, 88, 95]
})

print("Total number of students: ",len(df["Name"]))
print('Average age: ',np.average(df["Age"]))
print("Average marks: ",np.average(df["Marks"]))
print("Student(s) with marks above 90: \n",df[df["Marks"] > 90])
print("Student(s) whose age is 20: \n",df[df["Age"] == 20])
df["Grade"] = np.select(
    [
        df["Marks"] >= 90,
        df["Marks"] >= 80
    ],
    [
        "A",
        "B"
    ],
    default="C"
)
print(df)