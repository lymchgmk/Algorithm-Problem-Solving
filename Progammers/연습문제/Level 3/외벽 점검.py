from collections import deque


def solution(n, weak, dist):
    def how_many_fix(s, d):
        res = []
        for i in range(-d+1, d):
            tmp = deque(range(1, n+1))
            tmp.rotate(-tmp.index(s) + i)
            if not is_fixed[tmp[0]]:
                res.append(tmp[0])
        return res
        
    is_fixed = {f: False if f in weak else True for f in range(1, n+1)}
    answer = 0
    while dist:
        d = dist.pop()
        answer += 1
        need_fix = [how_many_fix(s, d) for s in weak]
        for nf in need_fix:
            if not nf:
                need_fix.remove(nf)
        need_fix.sort(key=lambda x: (-len(x), -(max(x)-min(x))))
        pick = need_fix[0]
        for p in pick:
            is_fixed[p] = True
        if all(is_fixed.values()):
            return answer
    return -1


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n, weak, dist))
