import sys
from queue import PriorityQueue


PQ = PriorityQueue()
test = [1, 2, 3]
for t in test:
    print(t)
    PQ.put(-t)

for _ in range(len(test)):
    print(PQ.get())