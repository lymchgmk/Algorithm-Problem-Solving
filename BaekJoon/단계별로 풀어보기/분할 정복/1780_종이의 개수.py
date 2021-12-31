import sys
sys.stdin = open("1780_종이의 개수.txt", "rt")


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
count = [0, 0, 0]

def same(x, y, n):
    chk = paper[x][y]
    for i in range(n):
        for j in range(n):
            if paper[x+i][y+j] != chk:
                return False
    return True


def cut_tri(x, y, n):
    global count
    if n == 1 or same(x, y, n):
        count[paper[x][y]+1] += 1
        return
    else:
        cut_tri(x, y, n//3)
        cut_tri(x, y + n//3, n//3)
        cut_tri(x, y + 2*(n//3), n//3)
        cut_tri(x + n//3, y, n//3)
        cut_tri(x + n//3, y + n//3, n//3)
        cut_tri(x + n//3, y + 2*(n//3), n//3)
        cut_tri(x + 2*(n//3), y, n//3)
        cut_tri(x + 2*(n//3), y + n//3, n//3)
        cut_tri(x + 2*(n//3), y + 2*(n//3), n//3)
        

cut_tri(0, 0, N)
print(*count, sep = "\n")