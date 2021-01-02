input=__import__('sys').stdin.readline
Max=float('INF')
for __ in range(int(input())):
    n,m,k=map(int,input().split())
    D=[[] for _ in range(n+1)]
    for i in range(k):
        u,v,c,d=map(int,input().split())
        D[u].append((v,c,d))
    S=[[Max]*(m+1) for _ in range(n+1)]
    S[1][0]=0
    for e in range(m+1):
        for x in range(1,n+1):
            if S[x][e]==Max:continue
            t=S[x][e]
            for nx,ne,nt in D[x]:
                if ne+e>m:continue
                S[nx][ne+e]=min(S[nx][ne+e],t+nt)
    k=min(S[n])
    print([k,'Poor KCM'][k==Max])