import sys
sys.stdin = open('15649_N과 M (1).txt', 'rt')


from itertools import permutations


N, M = map(int, input().split())
N_list = range(1, N+1)
for perm in permutations(N_list, M):
    print(*perm)