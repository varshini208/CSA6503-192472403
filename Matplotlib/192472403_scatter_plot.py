import matplotlib.pyplot as plt

x = list(map(int, input("Enter x values: ").split()))
y = list(map(int, input("Enter y values: ").split()))

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()