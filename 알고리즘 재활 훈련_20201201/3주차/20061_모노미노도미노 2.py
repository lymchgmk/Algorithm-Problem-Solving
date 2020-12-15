import sys
sys.stdin = open('20061_모노미노도미노 2.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


N = int(input())
for _ in range(N):
    t, x, y = map(int, input())