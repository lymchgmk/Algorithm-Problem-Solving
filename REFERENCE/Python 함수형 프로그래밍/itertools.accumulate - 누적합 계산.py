from itertools import accumulate


test = [111, 222, 333]
result = accumulate(test)
print(result)
print(list(result))


test = ['a', 'b', 'c']
result = accumulate(test, lambda x, y: y+x)
print(list(result))