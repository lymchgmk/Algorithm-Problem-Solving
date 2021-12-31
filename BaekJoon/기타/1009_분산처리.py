import sys
from collections import defaultdict
sys.stdin = open('1009_분산처리.txt', 'rt')
input = lambda: sys.stdin.readline()


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10

    num = 1
    res = defaultdict(lambda: False)
    for _ in range(b):
        num = (num * a) % 10
        if not res[num]:
            res[num] = True
        else:
            break

    idx = b%len(res)-1
    ans = list(res.keys())[idx]
    print(ans if ans else 10)
