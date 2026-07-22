import matplotlib.pyplot as plt

x = list(map(int, input("Enter x values: ").split()))
y = list(map(int, input("Enter y values: ").split()))

plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
