import matplotlib.pyplot as plt

data = list(map(int, input("Enter values: ").split()))

plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()