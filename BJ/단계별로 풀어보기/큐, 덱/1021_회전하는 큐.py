import sys
sys.stdin = open('1021_회전하는 큐.txt', 'rt')


from collections import deque


input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
JM = list(map(int, input().split()))
deq = deque(list(range(1, N+1)))


def oper(deq):
    cnt, idx, result = 0, 0, []
    while result != JM:
        test = JM[idx]
        if test == deq[0]:
            result.append(deq.popleft())
            idx += 1
        else:
            deq_idx = deq.index(test)
            r, l = deq_idx, len(deq) - deq_idx
            if r > l:
                deq.rotate(-r)
            else:
                deq.rotate(l)
            cnt += min(r, l)

    return cnt


print(oper(deq))
