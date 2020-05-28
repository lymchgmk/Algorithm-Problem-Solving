import sys
sys.stdin=open('5653_줄기세포배양.txt')

T=int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # N: 세로, M: 가로
    petri_dish = [[0 for _ in range(M+K)] for _ in range(N+K)]
    inactive = []
    active = []
    dead = []