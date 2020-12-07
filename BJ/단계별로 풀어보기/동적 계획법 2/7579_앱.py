import sys
sys.stdin = open("7579_앱.txt", "rt")
input = lambda: sys.stdin.readline().strip()


N, M = map(int, input().split())
M = list(map(int, input().split()))
C = list(map(int, input().split()))

print(M)
print(C)