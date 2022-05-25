import numpy as np


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]).reshape(3, 4)

print(a, "\n")

print(a[0][0])
print(a[0, 0])

a[0][0] = 10
a[0, 1] = 20

print(a)