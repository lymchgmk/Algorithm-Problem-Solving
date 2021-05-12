def powerset(n, k, cursum):
    if ans < cursum: return
    if n == k:
        calc(n, k, cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum + h[k])
        A[k] = 0
        powerset((n, k+1, cursum))