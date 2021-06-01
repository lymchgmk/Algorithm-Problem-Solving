arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
two_powers = [2**x for x in range(0, 11)]


def chk_quad(N, start):
    print(start)
    x, y = start
    chk = arr[x][y]
    for i in range(N):
        for j in range(N):
            if arr[x+i][y+j] != chk:
                return -1
    return chk

ans = [0, 0]
def sol(arr, start):
    global ans
    N = len(arr)
    x, y = start
    test = [(x, y), (x, y + N//2), (x + N //2, y), (x+N//2, y+N//2)]
    next_test = []
    for t in test:
        temp = chk_quad(N//2, t)
        if temp != -1:
            ans[temp] += 1
        else:
            sol(arr, t)

    return ans

print(sol(arr, (0, 0)))