import sys
sys.stdin = open('1934_최소공배수.txt', 'rt')


def euclidean_algorithm(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    gcd = euclidean_algorithm(A, B)
    print(A*B//gcd)