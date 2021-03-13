import collections

deq = collections.deque([0] * 4, maxlen=4)
print(deq)
deq.append(100)
print(deq)
deq.append(100)
print(deq)
deq.appendleft(200)
print(deq)