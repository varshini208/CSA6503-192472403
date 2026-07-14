import pandas as pd
data = {
    "Name": ["Sai", "Ram", "Anu"],
    "Age": [20, 21, 19]
}
df = pd.DataFrame(data)
column = input("Enter column name: ")
print(df[column])