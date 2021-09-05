from itertools import cycle


test = ['a', 'b', 'c']
cycle_test = cycle(test)

for _ in range(12):
    # print(cycle_test.__next__())
    print(next(cycle_test))
