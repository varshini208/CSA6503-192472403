import matplotlib.pyplot as plt

labels = input("Enter labels: ").split()
sizes = list(map(int, input("Enter values: ").split()))

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()