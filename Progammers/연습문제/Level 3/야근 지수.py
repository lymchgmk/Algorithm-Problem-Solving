def solution(n, works):
    import heapq
    
    if sum(works) <= n:
        return 0
    
    works = [-work for work in works]
    heapq.heapify(works)
    while n:
        tmp = heapq.heappop(works)
        heapq.heappush(works, tmp+1)
        n -= 1
    
    return sum([work**2 for work in works])

n = 4
works = [4, 3, 3]
# 580
print(solution(n, works))