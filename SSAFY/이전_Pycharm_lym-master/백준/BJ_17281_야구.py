import sys
sys.stdin = open("BJ_17281_야구.txt", "r")

N = int(input())
innings =[list(map(int, input().split())) for _ in range(N)]
# 타순 최적으로 정하고 (아마 sort?) /  0 3번 만날때까지 돌리면 끝
# 4번 타자 조심
idx = 0
fourth_hitter = innings[idx].pop(0)
innings[idx].insert(fourth_hitter, 4)
hitters = []
next = 0
while hitters.count(0) != 3*N:
    temp1 = []
    temp2 = innings[idx] * 2
    temp1.extend(temp2)

    my_inning = temp1[9 - next : 18 + 1 - next]
    keep_going = my_inning[:]

    while hitters.count(0) != 3:
        hitters.append(keep_going.pop(0))

        if len(keep_going) == 0:
            keep_going = my_inning[:]

    # 다음 이닝으로 넘어가는 경우
    next = 9 - len(keep_going)
    idx += 1

print(hitters)
# 아웃 후에 다음이닝에서 순서가 안 이어짐



