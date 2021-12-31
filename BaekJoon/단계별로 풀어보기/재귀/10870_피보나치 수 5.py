import sys
sys.stdin = open('10870_피보나치 수 5.txt', 'rt')


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)


N = int(input())
print(fibo(N))