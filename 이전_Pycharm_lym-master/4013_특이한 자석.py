import sys
sys.stdin = open('4013_특이한 자석.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    K = int(input())
    mag = []
    rotate = []
    sum = 0
    for i in range(4):
        mag.append(list(map(int, input().split())))
    for i in range(K):
        rotate.append(list(map(int, input().split())))
#
    # print(mag)
    # print(rotate)
# 인접한 자석이 움직이는 경우 어떻게 할 건지 포함안되어있음
    for r in range(K):
        if rotate[r][0] == 1:
            if rotate[r][1] == 1:
                mag[1]
            elif rotate[r][0] == -1:
                mag[1]

        elif rotate[r][0] == 2:
            if rotate[r][1] == 1:
                mag[2]
            elif rotate[r][0] == -1:
                mag[2]

        elif rotate[r][0] == 3:
            if rotate[r][1] == 1:
                mag[3]
            elif rotate[r][0] == -1:
                mag[3]

        elif rotate[r][0] == 4:
            if rotate[r][1] == 1:
                mag[4]
            elif rotate[r][0] == -1:
                mag[4]
