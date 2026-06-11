import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [85, 92, 78]
})
df["Result"] = np.where(df["Marks"] >= 80, 'Pass','Fail')
print(df)