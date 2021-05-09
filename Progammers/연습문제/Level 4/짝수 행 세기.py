def solution(a):
    L = len(a[0])
    for i in range(L):
        col = [row[i] for row in a]
        print(col)


a = [[0,1,0],[1,1,1],[1,1,0],[0,1,1]]
print(solution(a))
