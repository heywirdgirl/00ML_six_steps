import numpy as np

# Create a rank 1 array
a = np.array([0, 1, 2])
print(type(a))

# this will print the dimension of the array
print(a.shape)
print(a[0])
print(a[1])
print(a[2])

# Change an element of the array
a[0] = 5
print(a)
# ----output-----
# <type 'numpy.ndarray'>
# (3L,)
# 1
# 2
# 3
# [5 2 3]

# Create a rank 2 array
b = np.array([[0,1,2],[3,4,5]])
print(b.shape)
print(b)
print(b[0, 0],b[0, 1],b[1, 0])
# ----output-----
# (2L, 3L)
# [[0 1 2]
#  [3 4 5]]
# 0 1 3



