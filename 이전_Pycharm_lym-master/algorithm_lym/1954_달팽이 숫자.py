import sys
sys.stdin = open("1954_달팽이 숫자.txt", "r")

def snail(num):
    mtrx = [[0 for _ in range(num)] for _ in range(num)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, -1
    c = 1
    for i in range(num + num -1):
        for j in range((num + num -i)//2):
            x += dx[i % 4]
            y += dy[i % 4]
            mtrx[x][y] = c
            c += 1
    return mtrx

for i in snail(5):
    print(*i)


