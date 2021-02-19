def H(n, r, q):
    if r == 0:
        print(T)
    elif n == 0:  # n < r
        return
    else:
        T[r-1] = A[n-1]
        H(n, r-1, q)
        H(n-1, r, q)

A =[1,2,3,4]
T =[0] * 3

H(4,3,3)
