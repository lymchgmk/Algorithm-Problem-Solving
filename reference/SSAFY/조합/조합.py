def myprint():
    for i in range(K):
        print(T[i], end = " ")
    print()

def comb(n, r):
    if r == 0:
        myprint()
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

N, K = map(int, input().split())

A = range(1, N+1)
T =[0] * K
comb(N, K)
