from bisect import bisect_left, bisect_right

t = 10
target = [1, 2, 2, 4, 5, 5, 5, 6]

print(bisect_left(target, t))
print(bisect_right(target, t))
