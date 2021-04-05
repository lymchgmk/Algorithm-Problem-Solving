from collections import deque


def solution(n, weak, dist):
    def how_many_fix(s, d):
        res = set([s])
        for i in range(-d + 1, d):
            tmp = deque(range(n))
            tmp.rotate(-tmp.index(s) + i)
            if not is_fixed[tmp[0]]:
                res.add(tmp[0])
        return res
    
    is_fixed = {f: False if f in weak else True for f in range(n)}
    answer = 0
    dist.sort()
    while dist:
        d = dist.pop()
        answer += 1
        need_fix = [how_many_fix(s, d) for s in weak]
        for nf in need_fix:
            if not nf:
                need_fix.remove(nf)
                
        need_fix.sort(key=lambda x: (-len(x), -(max(x) - min(x))))
        
        pick = need_fix[0]
        print(pick)
        for p in pick:
            is_fixed[p] = True
            
        if all(is_fixed.values()):
            return answer
    return -1


# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]
3
print(solution(n, weak, dist))
