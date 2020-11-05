import sys
sys.stdin = open("1932_정수 삼각형.txt", 'rt')


n = int(input())
t = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        print(j) 