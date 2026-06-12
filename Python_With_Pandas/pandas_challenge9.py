import pandas as pd
import numpy as np
students = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Rahul", "Priya", "Amit", "Karan"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [85, 92, 78, 88]
})

print("Students: \n",students)
print("Marks: \n",marks)
merge = pd.merge(
    students,
    marks,
    on="ID"
)
print("Merge DataFrame: \n",merge)
print("Print only students with Marks > 80: \n",merge[merge["Marks"] > 80]["Name"].values)
print("average marks: ",np.average(merge["Marks"]))
print("student with the highest marks: ",merge.loc[merge["Marks"].idxmax(), "Name"])