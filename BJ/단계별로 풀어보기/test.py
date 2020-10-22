# import sys
# sys.stdin = open('', 'rt')

import numpy as np

a = np.random.randn(4, 3)
b = np.random.randn(3, 2)
c = a*b

print(c.shape)