import heapq
import random



if __name__ == "__main__":
    tmp1 = [8, 1, 3, 2, 4, 5, 6, 7, 9, 10, 11]
    tmp2 = [-x for x in tmp1]
    heapq.heapify(tmp1)
    heapq.heapify(tmp2)
    add1 = []
    add2 = []
    for _ in range(3):
        add1.append(heapq.heappop(tmp1))
        add2.append(heapq.heappop(tmp2))

    print(heapq.heappop(tmp1))
    print(heapq.heappop(tmp2))

    for _ in range(3):
        heapq.heappush(tmp1, add1.pop())
        heapq.heappush(tmp2, add2.pop())