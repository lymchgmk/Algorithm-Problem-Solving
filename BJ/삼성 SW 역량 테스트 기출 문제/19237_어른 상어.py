import sys
sys.stdin = open("19237_어른 상어.txt", "r")

N, M, k = map(int, input().split())
sharks_arr = [list(map(int, input().split())) for _ in range(N)]
dirs = list(map(int, input().split()))
dirs_priority = [list(map(int, input().split())) for _ in range(4*M)]
# 1, 2, 3, 4
# 상, 하, 좌, 우

time_count = 0
is_sharks = M
while is_sharks != 1:
    pass
