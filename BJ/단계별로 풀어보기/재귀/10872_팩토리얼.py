import sys
sys.stdin = open('10872_팩토리얼.txt', 'rt')


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


N = int(input())
print(factorial(N))
