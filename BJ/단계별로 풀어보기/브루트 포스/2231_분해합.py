import sys
sys.stdin = open('2231_분해합.txt', 'rt')


N = int(input())
for n in range(N):
    if sum(list(map(int, str(n)))) + n == N:
        print(n)
        break
else:
    print(0)