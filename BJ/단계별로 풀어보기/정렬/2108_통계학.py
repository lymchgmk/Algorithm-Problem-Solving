import sys
sys.stdin = open('2108_통계학.txt', 'rt')

import sys
from collections import Counter


def input():
    return sys.stdin.readline()

N = int(input())
numbers = []
ans_sum = 0
for _ in range(N):
    num = int(input())
    numbers.append(num)
    ans_sum += num

if N == 1:
    print(numbers[0])
    print(numbers[0])
    print(numbers[0])
    print(0)
else:
    numbers.sort()
    print(round(ans_sum / N))
    print(numbers[N//2])
    cnt = Counter(numbers).most_common()
    print(cnt[1][0] if cnt[0][1]==cnt[1][1] else cnt[0][0])
    print(numbers[N-1] - numbers[0])