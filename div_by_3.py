import numpy as np

M = np.arange(1,101).reshape(10,10)
A = M**2
D = A[A%3 == 0]