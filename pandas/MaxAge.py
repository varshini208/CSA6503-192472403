import pandas as pd
data = {
    "Name": ["Sai", "Ram", "Anu"],
    "Age": [20, 21, 19]
}
df = pd.DataFrame(data)
print("Maximum Age =", df["Age"].max())