import sys
sys.stdin = open("BJ_17136_색종이 붙이기.txt")

def issafe():
    if 0 <= i <L and 0 <= j <L:
        return True
    else:
        return False


def colored_paper((i, j), N):
    check_arr = [[0 for _ in range(N)] for _ in range(5)]
    for k in range(N):
        for l in range(N):
            if arr[i+k][j+l] == 1:
                check_arr[i+k][j+k] += 1
    if sum(check_arr) == N**2:
        result += 1


T = 10
data = [list(map(int, input().split())) for _ in range(10)]
L = len(data)
result = 0

while
