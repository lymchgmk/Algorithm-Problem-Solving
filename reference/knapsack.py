'''
물건 베낭무게, 각각 무게 가치
입력:
3
3 30
25 10
10 9
10 5
3 30
25 15
10 9
10 5
3 30
5 50
10 60
20 140

출력:
#1 14
#2 15
#3 200
'''
def powerset(n, k, currV, currC):  # n:물건개수, k:depth, currV:현재무게합, currC:현재가치합
    global ans
    if currV > K: return  # 현재 무게가 베낭무게보다 크면

    if n == k:
        if ans < currC: ans = currC
    else:
        A[k] = 1
        powerset(n, k+1, currV + V[k], currC + C[k])
        A[k] = 0
        powerset(n, k+1, currV, currC)

import sys
sys.stdin = open("knapsack_input.txt", "r")
T = int(input())

for tc in range(T):
    N, K = map(int, input().split())    # 물건갯수, 베낭무게
    V = [0] * N                         # 각 물건의 무게
    C = [0] * N                         # 각 물건의 가치
    A = [0] * N                         # 부분집합 포함 여부
    ans = 0

    for i in range(N):
        V[i], C[i] = map(int, input().split())

    powerset(N, 0, 0, 0)
    print("#%d %d" % (tc+1, ans))



# 0-1 배낭문제 : 짐을 쪼갤 수 없는 경우의 배낭 문제
def zero_one_knapsack(cargo):
    capacity = 15
    pack = []
    
    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])
        
    return pack[-1][-1]
