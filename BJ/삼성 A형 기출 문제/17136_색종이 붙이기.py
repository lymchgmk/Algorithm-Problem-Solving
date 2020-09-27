import sys
from copy import deepcopy
#sys.stdin=open("17136_색종이 붙이기.txt")

def issafe(x, y, field):
    if 0<= x < len(field) and 0<= y < len(field[0]):
        return True
    else:
        return False

def sum_list(lst):
    res=0
    for i in lst:
        if type(i)==list:
            res+=sum_list(i)
        else:
            res+=i
    return res


def confetti(field, node, num):
    global board

    for i in range(num):
        for j in range(num):
            if not issafe(node[0] + i, node[1] + j, board) or board[node[0] + i][node[1] + j] == 0:
                return 0

    for i in range(num):
        for j in range(num):
            board[node[0] + i][node[1] + j] = 0
    return 1

def check_count(counts):
    for count in counts:
        if count>5:
            return False
    return True

data=[list(map(int, input().split())) for _ in range(10)]

board=deepcopy(data)
confetti_count=[0]*6
n=5
for n in range(5, 0, -1):
    if n != 1:
        for i in range(10):
            for j in range(10):
                if issafe(i, j+1, board) and issafe(i+1, j, board):
                    if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1]==1:
                        start=[i, j]
                        confetti_count[n] += confetti(board, start, n)

    else:
        for i in range(10):
            for j in range(10):
                if board[i][j] == 1:
                    confetti_count[1]+=1
                    board[i][j]=0

if sum_list(board) != 0 or not check_count(confetti_count):
    print(-1)

else:
    print(sum(confetti_count))



def DFS(depth):
    global my_min

    if depth >= my_min:
        return

    for r in range(10):
        for c in range(10):
            print(100, r, c)
            if my_map[r][c]:
                break
            else:
                print(0, r, c)
                continue
        break
        

my_map = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
INF = float('inf')
my_min = INF
# DFS(0)
# print(-1 if my_min == INF else my_min)

for r in range(10):
    for c in range(10):
        print(100, r, c)
        if my_map[r][c]:
            break
        else:
            print(0, r, c)
            continue
    break