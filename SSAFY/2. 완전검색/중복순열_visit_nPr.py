# 3P2

def perm(n, r, k):
    if r == k:
        print(t)
    else:
        for i in range(0, n):
            # if visited[i] : continue
            t[k] = a[i]
            # visited[i] = True
            perm(n, r, k+1)
            # visited[i] = False


a = [1, 2, 3]
t = [0] * 2
visited = [0] * 3
perm(3, 2, 0)
