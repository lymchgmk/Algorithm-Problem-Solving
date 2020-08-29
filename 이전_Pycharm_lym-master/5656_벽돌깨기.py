import sys
sys.stdin = open("5656_벽돌깨기.txt", "r")

T =int(input())

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = []
    for height in range(H):
        brick.append(list(map(int, input().split())))
#
    # 메커니즘 생각해볼것