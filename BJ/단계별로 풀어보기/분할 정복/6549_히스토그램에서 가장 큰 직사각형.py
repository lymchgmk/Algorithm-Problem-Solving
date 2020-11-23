import sys
sys.stdin = open("6549_히스토그램에서 가장 큰 직사각형.txt", "rt")


input = lambda: sys.stdin.readline().strip()
while True:
    h = list(map(int, input().split()))
    n = h[0]
    if h == [0]:
        break

    