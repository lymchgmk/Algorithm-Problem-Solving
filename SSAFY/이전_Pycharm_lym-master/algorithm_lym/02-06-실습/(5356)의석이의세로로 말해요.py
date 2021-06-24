import sys
sys.stdin = open("(5356)의석이의세로로 말해요_input.txt")
T = int(input())

for tc in range(1, T+1):
    data = [''] * 5
    maxV = 0

    for i in range(5):  #제일 긴 단어 찾기
        data[i] = input()
        if(maxV < len(data[i])): maxV = len(data[i])

    print("#{}".format(tc), end=" ")
    for i in range(maxV):
        for j in range(5):
            if len(data[j]) <= i: continue
            print(data[j][i], end="")
    print()
