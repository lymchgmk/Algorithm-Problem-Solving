import sys, collections
sys.stdin = open("5099.피자굽기.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    pizza=[[idx+1, val] for idx, val in enumerate(Ci)]
    furnace = collections.deque()
    ans=[]

    for i in range(N):
        furnace.appendleft(pizza.pop(0))

    while furnace:
        # 피자 판 회전
        temp=furnace.pop()
        furnace.appendleft(temp)

        check=furnace.popleft()
        check_cheese=check[1]
        if (check_cheese//2) == 0:
            ans.append(check[0])
            if pizza:
                furnace.appendleft(pizza.pop(0))
        else:
            furnace.appendleft([check[0], check_cheese//2])

    print(f'#{test_case} {ans[-1]}')