import sys
sys.stdin = open('15652_N과 M (4).txt', 'rt')


from itertools import combinations_with_replacement


N, M = map(int, input().split())
N_list = range(1, N+1)

for cwr in combinations_with_replacement(N_list, M):
    print(*cwr)