import sys
sys.stdin = open('1011_Fly me to the Alpha Centauri.txt', 'rt')


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    x, y = 0, y-x-1
    dist, k = 0, 0
    while dist != y:
        k_list = []