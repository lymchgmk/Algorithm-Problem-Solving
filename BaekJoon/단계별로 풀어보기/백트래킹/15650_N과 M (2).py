import sys
sys.stdin = open('15650_N과 M (2).txt', 'rt')


from itertools import combinations


N, M = map(int, input().split())
N_list = range(1, N+1)
for comb in combinations(N_list, M):
    print(*comb)