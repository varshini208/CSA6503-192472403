import pandas as pd
data = {
    "Name": ["Sai", "Ram", "Anu", "Ravi", "Priya"],
    "Age": [20, 21, 19, 22, 18]
}
df = pd.DataFrame(data)
n = int(input("Enter number of rows to display: "))
print(df.head(n))