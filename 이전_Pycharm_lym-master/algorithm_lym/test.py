import sys
sys.stdin = open("test.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    col = []
    for i in range(N):
        col.append([row[i] for row in table])


    for i in range(N):
        N_mag = []
        S_mag = []
        for j in range(N):
            if col[i][j] == 1:
                N_mag.append([j, "N"])
            elif col[i][j] == 2:
                S_mag.append([j, "S"])

        mag = N_mag + S_mag
        mag.sort()
        #print(mag)

        for k in range(len(mag)):

