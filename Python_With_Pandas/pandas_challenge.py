import pandas as pd
data = pd.DataFrame(
    {
        "Name": ["Rahul", "Priya", "Amit"],
        "Age": [20, 19, 21],
        "Marks": [85, 92, 78]
    }
)
print("Entire DataFrame: \n",data)
print("Name column: \n",data["Name"])
print("Marks column: \n",data["Marks"])
print("First row: \n",data.iloc[0])
