from itertools import product

_list = [['-', 'java', 'python', 'cpp'], ['-', 'backend', 'frontend'], ['-', 'junior', 'senior'], ['-', 'pizza', 'chicken']]
print(list(product(*_list)))