def checkCard():
    for i in range(4):
        for j in range(13):
            if count[i][j] > 1:
                return 0
            elif count[i][j] == 1:
                ans[i] += 1

    return 1

import sys
sys.stdin = open("(4047)영준이의_카드_카운팅_input.txt")

T = int(input())
for tc in range(T):
    count = [[0 for _ in range(13)] for _ in range(4)]
    ans = [0 for _ in range(4)]
    str = input()
    flag = 1

    for i in range(0, len(str), 3):
        row = 0
        sdhc = str[i]
        col = int(str[i+1] + str[i+2])

        if sdhc == "S": row = 0
        elif sdhc == "D": row = 1
        elif sdhc == "H": row = 2
        elif sdhc == "C": row = 3

        count[row][col-1] += 1

    flag = checkCard()

    print("#{}".format(tc+1), end= " ")
    if flag == 0: print("ERROR", end=" ")
    else:
        for i in range(4):
            print(13-ans[i] , end = " ")
    print()