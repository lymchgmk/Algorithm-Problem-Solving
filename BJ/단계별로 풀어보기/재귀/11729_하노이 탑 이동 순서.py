import sys
sys.stdin = open('11729_하노이 탑 이동 순서.txt', 'rt')


def hanoi(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


N = int(input())
print(hanoi(N))
