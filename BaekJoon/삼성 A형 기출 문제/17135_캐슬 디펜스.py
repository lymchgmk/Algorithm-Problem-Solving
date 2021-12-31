import sys
from copy import deepcopy
from itertools import combinations
sys.stdin=open("17135_캐슬 디펜스.txt")

def sum_list(lst, res=0):
    for i in lst:
        if type(i)==list:
            res+=sum_list(i)
        else:
            res+=i
    return res

def aim(field, archer, D):
    return_aim=[]
    enemys = [[i, j] for i in range(len(field)) for j in range(len(field[0])) if field[i][j] == 1]
    for enemy in enemys:
        distance=abs(len(field)-enemy[0]) + abs(enemy[1]-archer)
        if distance <= D:
            return_aim.append([distance, enemy])
    if return_aim:
        return_aim.sort(key=lambda x : (x[0], x[1][1]))
        return return_aim[0][1]

def castle_defense(field, archers):
    global D
    count=0
    while field and sum_list(field):
        arrow = []
        for archer in archers:
            temp=aim(field, archer, D)
            if temp != None and temp not in arrow:
                arrow.append(temp)

        for shot in arrow:
            field[shot[0]][shot[1]]=0

        count+=len(arrow)

        del field[-1]

    return count

N, M, D = map(int, input().split())
data=[list(map(int, input().split())) for _ in range(N)]

archers_list=combinations(range(M), 3)

ans=0
for archers in archers_list:
    field=deepcopy(data)
    solve=castle_defense(field, archers)
    if ans < solve:
        ans=solve

print(ans)