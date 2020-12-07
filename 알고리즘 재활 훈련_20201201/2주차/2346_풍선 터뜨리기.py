import sys
sys.stdin = open('2346_풍선 터뜨리기.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


N = int(input())
balloon = deque(enumerate(list(map(int, input().split()))))
answer = []
while balloon:
    idx, val = balloon.popleft()
    answer.append(idx+1)
    if val > 0:
        balloon.rotate(-val+1)
    elif val < 0:
        balloon.rotate(-val)

print(*answer)
