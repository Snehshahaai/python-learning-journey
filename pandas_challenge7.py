import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Karan"],
    "Marks": [85, np.nan, 78, 92],
    "Age": [20, 19, np.nan, 22]
})

print("Entire DataFrame:\n", df)

print("\nRows containing missing values:\n",
      df[df.isnull().any(axis=1)])

print("\nNumber of missing values in each column:\n",
      df.isnull().sum())

print("\nDataFrame after replacing missing values with 0:\n",
      df.fillna(0))

print("\nDataFrame after dropping rows with missing values:\n",
      df.dropna())