import sys
from itertools import permutations
from copy import deepcopy
sys.stdin=open("17406_배열 돌리기4.txt")

def arr_value(array):
    sum_list=[sum(row) for row in array]
    return min(sum_list)

def rotate(operator):
    global array
    dirs=[(0, 1), (1, 0), (0, -1), (-1, 0)]
    center=(operator[0]-1, operator[1]-1)
    shell=1
    while shell != operator[2]+1:
        x_start, y_start = center[0]-shell, center[1]-shell
        x_now, y_now = x_start, y_start
        temp = array[x_now][y_now]
        for i in range(8*shell):
            dir=dirs[i//(2*shell)]
            x_next, y_next = x_now+dir[0], y_now+dir[1]
            array[x_next][y_next], temp = temp, array[x_next][y_next]

            x_now, y_now = x_next, y_next
        shell+=1

N, M, K = map(int, input().split())
data=[list(map(int, input().split())) for _ in range(N)]
operators=[list(map(int, input().split())) for _ in range(K)]

procedures=permutations(range(K))

ans=100*50*50
for procedure in procedures:
    array=deepcopy(data)
    for idx in procedure:
        rotate(operators[idx])

    solve=arr_value(array)
    if solve < ans:
        ans=solve

print(ans)
