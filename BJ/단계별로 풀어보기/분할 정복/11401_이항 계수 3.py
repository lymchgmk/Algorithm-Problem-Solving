import sys
sys.stdin = open("11401_이항 계수 3.txt", "rt")


p = 1000000007
def power(a, n):
    if n == 0:
        return 1
    
    if n % 2 == 1:
        return (power(a, n//2)**2 * a) % p
    else:
        return (power(a, n//2)**2) % p


input = lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())

f = [1]*(N+1)
for i in range(2, N+1):
    f[i] = f[i-1]*i % p

numerator = f[N] % p
denominator = (f[K] * f[N-K]) % p
print((numerator * power(denominator, p-2) % p) % p)