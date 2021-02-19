def perm(n, k):
    if n == k:
        print(t)
    else:
        for i in range(0, n):
            # if visited[i] : continue
            t[k] = a[i]
            # visited[i] = True
            perm(n, k+1)
            # visited[i] = False

a = [1, 2, 3]
t = [0] * 3
visited = [0] * 3
perm(3, 0)
