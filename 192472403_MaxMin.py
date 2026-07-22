import numpy as np
a = np.array(list(map(int, input("Enter array elements: ").split())))
print("Maximum =", np.max(a))
print("Minimum =", np.min(a))