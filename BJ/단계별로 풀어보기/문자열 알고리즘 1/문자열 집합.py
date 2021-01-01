import sys
sys.stdin = open('문자열 집합.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


N, M = map(int, input().split())
S = [input() for _ in range(N)]
test = [input() for _ in range(M)]


result = 0
for t in test:
    if t in S:
        result += 1

print(result)