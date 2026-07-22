import pandas as pd
data = {
    "Name": ["Sai", "Ram", "Anu"],
    "Age": [20, 21, 19]
}
df = pd.DataFrame(data)
marks = list(map(int, input("Enter 3 marks: ").split()))
df["Marks"] = marks
print(df)