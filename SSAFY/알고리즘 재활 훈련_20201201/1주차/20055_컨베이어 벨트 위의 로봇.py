import sys
sys.stdin = open("20055_컨베이어 벨트 위의 로봇.txt", "rt")
input = lambda: sys.stdin.readline().strip()
from collections import deque


def send_down_robot():
    global belt
    if belt[N-1][1] == True:
        belt[N-1][1] = False


N, K = map(int, input().split())
A = list(map(int, input().split()))

belt = deque()
for i in range(2*N):
    belt.append([A[i], False])

answer_cnt = 1
while True:
    #1
    belt.appendleft(belt.pop())
    send_down_robot()

    #2
    for i in range(N-2, -1, -1):
        if belt[i][1] == True and belt[i+1][1] == False and belt[i+1][0] >= 1:
            belt[i][1], belt[i+1][1] = False, True
            belt[i+1][0] -= 1
    send_down_robot()

    #3
    if belt[0][0] > 0:
        belt[0][1] = True
        belt[0][0] -= 1

    #4
    check_cnt = 0
    for i in range(2*N):
        if belt[i][0] == 0:
            check_cnt += 1
    if check_cnt >= K:
        print(answer_cnt)
        break

    answer_cnt += 1