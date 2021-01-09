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
