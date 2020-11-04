import sys
sys.stdin = open('9375_패션왕 신해빈.txt', 'rt')


T = int(input())
for _ in range(T):
    N = int(input())
    clothes = {}
    for _ in range(N):
        cloth, type = input().split()
        if type not in clothes.keys():
            clothes[type] = 1
        else:
            clothes[type] += 1
    answer = 1
    for v in clothes.values():
        answer *= v+1
    print(answer - 1)