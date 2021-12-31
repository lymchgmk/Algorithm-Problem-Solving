import sys
sys.stdin = open('7568_덩치.txt', 'rt')

N = int(input())
bulk = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
                rank += 1
    print(rank)

