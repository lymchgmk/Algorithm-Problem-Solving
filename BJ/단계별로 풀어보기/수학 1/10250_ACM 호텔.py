import sys
sys.stdin = open('10250_ACM 호텔.txt', 'rt')

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor, room = N%H, N//H + 1
    if floor == 0:
        floor,room = H, room-1
    answer = 100 * floor + room
    print(answer)