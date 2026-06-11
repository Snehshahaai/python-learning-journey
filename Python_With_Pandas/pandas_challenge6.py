import pandas as pd
import numpy as np
df = pd.read_csv("students.csv")
print("the entire DataFrame: \n",pd.DataFrame(df))
print("The Name column: \n",df["Name"])
print("students with marks above 90: \n",df[df["Marks"] > 90])
print("The average marks: \n",np.average(df["Marks"]))
top_student = df.loc[df["Marks"].idxmax(), "Name"]
print("the student with the highest marks: ",top_student)