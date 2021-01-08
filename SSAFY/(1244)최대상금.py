import time
start_time = time.time()

import sys
sys.stdin = open("(1244)최대상금_input.txt", "r")
T = int(input())
MAXSIZE = 720       # 6!

def swap(prize, i, j):
    #itoa
    numArr = [0] * numOfcard
    for k in range(numOfcard-1, -1, -1):
        numArr[k] = prize % 10
        prize //= 10

    #swap
    numArr[i], numArr[j] = numArr[j], numArr[i]

    # atoi
    prize = 0
    for k in range(numOfcard):
        prize = prize * 10 + numArr[k]

    return prize


def findMax(prize, num, k):
    global ans
    # 메모이제이션 및 가지치기
    # for i in range(MAXSIZE):
    #     if memo[k][i] == 0:
    #         memo[k][i] = prize
    #         break
    #     elif memo[k][i] == prize:
    #         return

    if k == num:
        if prize > ans: ans = prize
    else:
        for i in range(numOfcard-1):
            for j in range(i+1, numOfcard):
                findMax(swap(prize, i, j), num, k+1)


for tc in range(T):
    prize, num = map(int, input().split())      # 숫자판, 교환횟수
    memo = [[0] * MAXSIZE for _ in range(num+1)]# 메모이제이션
    numOfcard = 0                               # 숫자판의 숫자수
    ans = 0
    t = prize

    # 숫자판의 자리수 구하기
    while(t):
        t //=10
        numOfcard += 1

    #### Greedy ####
    # if num >= 6 :
    #     if num % 2 == 0 : num = 6
    #     else: num = 5

    findMax(prize, num, 0)

    print("#{} {}".format(tc+1, ans))

print(time.time() - start_time, 'seconds')


