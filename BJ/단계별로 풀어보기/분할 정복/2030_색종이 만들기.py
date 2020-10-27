import sys
sys.stdin = open("2030_색종이 만들기.txt", "rt")


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0


def divide(x, y, N):
    global white, blue
    count = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] == 1:
                count += 1
    if count == 0:
        white += 1
    elif count == N**2:
        blue += 1
    else:
        divide(x, y, N//2)
        divide(x, y+N//2, N//2)
        divide(x+N//2, y, N//2)
        divide(x+N//2, y+N//2, N//2)
    return

divide(0, 0, N)
print(white)
print(blue)
