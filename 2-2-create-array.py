# Create a 3x3 array of all zeros
import numpy as np

a = np.zeros((3,3))
print(a)
"""
----- output -----
[[ 0.  0.  0.]
[ 0.  0.  0.]
[ 0.  0.  0.]]
"""

# Create a 2x2 array of all ones
b = np.ones((2,2))
print(b)
"""
---- output ----
[[ 1.  1.]
[ 1.  1.]]
"""

# Create a 3x3 constant array
c = np.full((3,3), 7)
print(c)
"""
---- output ----
[[ 7.  7.  7.]
[ 7.  7.  7.]
[ 7.  7.  7.]]
"""

# Create a 3x3 array filled with random values
d = np.random.random((3,3))
print(d)
"""
---- output ----
[[ 0.85536712  0.14369497  0.46311367]
[ 0.78952054  0.43537586  0.48996107]
[ 0.1963929   0.12326955  0.00923631]]
"""

# Create a 3x3 identity matrix
e = np.eye(3)
print(e)
"""
---- output ----
[[ 1.  0.  0.]
[ 0.  1.  0.]
[ 0.  0.  1.]]
"""

# convert list to array
f = np.array([2, 3, 1, 0])
print(f)
"""
---- output ----
[2 3 1 0]
"""

# arange() will create arrays with regularly incrementing values
g = np.arange(20)
print(g)
"""
---- output ----
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
"""

# note mix of tuple and lists
h = np.array([[0, 1,2.0],[0,0,0],(1+1j,3.,2.)])
print(h)

# ????  create an array of range with float data type
"""
dtype=np.float
i = np.arange(1, 8,float)
print(i)
"""

# linspace() will create arrays with a specified number of items which are
# spaced equally between the specified beginning and end values
j = np.linspace(2., 4., 5)
print(j)




