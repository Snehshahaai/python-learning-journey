import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Employee": ["Rahul", "Priya", "Amit", "Neha", "Karan", "Riya"],
    "Salary": [50000, 60000, 45000, 55000, 40000, 42000]
})

print("Average Salary by Department:\n")
print(df.groupby("Department")["Salary"].mean())

print("\nMaximum Salary by Department:\n")
print(df.groupby("Department")["Salary"].max())

print("\nTotal Salary by Department:\n")
print(df.groupby("Department")["Salary"].sum())

print("\nEmployee Count by Department:\n")
print(df.groupby("Department")["Employee"].count())