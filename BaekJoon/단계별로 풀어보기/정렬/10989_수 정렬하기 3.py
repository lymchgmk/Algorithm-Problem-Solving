import sys
sys.stdin = open('10989_수 정렬하기 3.txt', 'rt')


N = int(input())
count = [0] * 10001

for i in range(N):
    n = int(sys.stdin.readline())
    count[n] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)