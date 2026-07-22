import pandas as pd
n = int(input("Enter number of students: "))
name = []
age = []
for i in range(n):
    name.append(input("Enter Name: "))
    age.append(int(input("Enter Age: ")))
data = {
    "Name": name,
    "Age": age
}
df = pd.DataFrame(data)
print(df)