def writeDiamond(c, col):
    ch[2][2] = c
    for i in range(5):
        for j in range(5):
            out[i][col+j] = ch[i][j]

import sys
sys.stdin = open("(4751)다솔이의다이아몬드장식_input.txt")
T = int(input())

#파이선은 문자가 따로 없으므로 한글자 문자열로 처리
ch = [['.','.','#','.','.'],['.','#','.','#','.'],['#','.','.','.','#'],['.','#','.','#','.'],['.','.','#','.','.']]
for tc in range(1, T+1):
    out = [["" for _ in range(250)]for _ in range(5)]
    data = list(input())

    writeDiamond(data[0], 0)
    col = 0
    for i in range(1, len(data)):
        col += 4
        writeDiamond(data[i], col)

    for i in range(5):
        for j in range(len(data)*5):
            print(out[i][j], end="")
        print()