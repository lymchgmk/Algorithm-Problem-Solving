import sys
sys.stdin = open("1992_쿼드트리.txt", "rt")


N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]


def same(x, y, n):
    chk = board[x][y]
    for i in range(n):
        for j in range(n):
            if board[x+i][y+j] != chk:
                return False
    return True


def quadtree(x, y, n):
    if n == 1 or same(x, y, n):
        return str(board[x][y])
    else:
        return "(" + quadtree(x, y, n//2) + quadtree(x, y + n//2, n//2) + quadtree(x + n//2, y, n//2) + quadtree(x + n//2, y + n//2, n//2) + ")"


print(quadtree(0, 0, N))