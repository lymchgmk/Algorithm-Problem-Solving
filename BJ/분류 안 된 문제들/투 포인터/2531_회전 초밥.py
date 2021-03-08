import sys
sys.stdin = open('2531_회전 초밥.txt', 'r')
import collections


input = lambda: sys.stdin.readline().strip()
N, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(N)]
sushis += sushis[:k-1]
s = 0
ate_sushi = collections.deque(sushis[:k])
how_many = len(set(ate_sushi))
L = len(sushis)
while s + k < L:
    ate_sushi.popleft()
    ate_sushi.append(sushis[s + k])
    ate_sushi_set = set(ate_sushi)
    ate_sushi_set.add(c)
    how_many = max(how_many, len(ate_sushi_set))
    s += 1

print(how_many)
