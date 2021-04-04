tmp = list(range(3))

from itertools import product

ttmp = [tmp for _ in range(len(tmp))]
print(ttmp)
print(list(product(*ttmp)))