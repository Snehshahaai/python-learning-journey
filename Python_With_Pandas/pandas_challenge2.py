import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [20, 19, 21],
    "Marks": [85, 92, 78]
})
print("Students with marks greater than 80: \n",df[df["Marks"] > 80])
print("Students with age greater than 19: \n",df[df["Age"] > 19])
print("Only the Name column for students with marks greater than 80: \n",df[df["Marks"] > 80]["Name"])
print("Average marks of all students: ",np.average(df["Marks"]))
print("Highest marks: ",np.max(df["Marks"]))