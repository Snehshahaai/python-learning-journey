import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Karan"],
    "Marks": [85, 92, 78, 88]
})

print("Original DataFrame:\n", df)

print("\nDataFrame sorted by Marks (ascending):\n",
      df.sort_values(by="Marks", ascending=True))

print("\nDataFrame sorted by Marks (descending):\n",
      df.sort_values(by="Marks", ascending=False))

top_student = df.loc[df["Marks"].idxmax(), "Name"]

print("\nName of the student with the highest marks:", top_student)