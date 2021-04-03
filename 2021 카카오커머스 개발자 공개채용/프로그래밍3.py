from itertools import combinations
from collections import deque


def solution(numbers, K):
    def check_diff(num_list, upper_bound):
        for n1, n2 in zip(num_list[:-1], num_list[1:]):
            if abs(n1-n2) > upper_bound:
                return False
        return True
    
    def swap(num_list, cnt):
        res = []
        for c1, c2 in combinations(range(len(num_list)), 2):
            tmp = num_list.copy()
            tmp[c1], tmp[c2] = tmp[c2], tmp[c1]
            res.append([tmp, cnt+1])
        return res
    
    deq = deque()
    cnt = 0
    deq.append([numbers, cnt])
    while deq:
        if cnt > len(numbers):
            return -1
        
        tmp, cnt = deq.popleft()
        for swapped in swap(tmp, cnt):
            num_list, cnt = swapped
            if check_diff(num_list, K):
                return cnt
            else:
                deq.append([num_list, cnt])


numbers = [100, 0]
k = 3
print(solution(numbers, k))