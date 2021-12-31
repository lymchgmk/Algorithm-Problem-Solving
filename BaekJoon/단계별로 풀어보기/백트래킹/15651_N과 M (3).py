import sys
sys.stdin = open('15651_N과 M (3).txt', 'rt')


from itertools import product


N, M = map(int, input().split())
N_list = range(1, N+1)
N_list_M = [N_list for _ in range(M)]
for prod in product(*N_list_M):
    print(*prod)