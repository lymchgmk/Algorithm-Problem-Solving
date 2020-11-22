import sys
sys.stdin = open("2749_피보나치 수 3.txt", "rt")


input = lambda: sys.stdin.readline().strip()
N = int(input())

fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
pisano_period = int(15*1000000/10)
sys.setrecursionlimit(pisano_period)


flag = False
if N > pisano_period:
    N %= pisano_period
    flag = True

if flag == True:
    L = pisano_period
else:
    L = N



def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)


print(fibo(N))