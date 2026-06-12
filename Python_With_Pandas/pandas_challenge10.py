import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Karan", "Neha", "Riya"],
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Marks": [85, 92, 78, 88, 95, 72],
    "Age": [20, 19, 21, 22, 20, 23]
})

print("Print the complete DataFrame.: \n",df)
print("Print students with Marks > 80. \n",df[df["Marks"] > 80]["Name"])
print("Print students whose Age is greater than 20. \n",df[df["Age"] > 20]["Name"])
df["Result"] = np.where(df["Marks"] >= 80,'Pass','Fail')
print(df)
print("Average Marks: ",df["Marks"].mean())
print("Highest Marks: ",df["Marks"].max())
print("Lowest Marks: ",df["Marks"].min())
print("Department-wise Average Marks. \n",df.groupby("Department")["Marks"].mean())
print("Top Student Name. ",df.loc[df['Marks'].idxmax(),"Name"])
print("Sort students by Marks in descending order. \n",df.sort_values("Marks",ascending=0))
df.to_csv("student_report.csv", index=False)
df1 = pd.read_csv("student_report.csv")
print("Final DataFrame from CSV: \n",df1)