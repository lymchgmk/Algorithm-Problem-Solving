from collections import deque


def solution(board, r, c):
    def cntl(board_str, cursor, dir):
        cntl_moved = (cursor[0] + dir[0], cursor[1] + dir[1])
        if 0 <= cntl_moved[0] < 4 and 0 <= cntl_moved[1] < 4:
            if board_str[4 * cntl_moved[0] + cntl_moved[1]] == "0":
                return cntl(board_str, cntl_moved, dir)
            else:
                return cntl_moved
        else:
            return cursor
    
    board_str = ""
    for i in range(4):
        for j in range(4):
            board_str += str(board[i][j])
            
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    deq = deque()
    deq.append((board_str, (r, c), 0, -1))
    visited_set = set()
    while deq:
        board_str, cursor, cnt, enter_pos = deq.popleft()
        
        visited = (board_str, cursor, cnt, enter_pos)
        if visited in visited_set:
            continue
        else:
            visited_set.add(visited)
            
        if board_str == "0"*16:
            return cnt
            
        for dir in dirs:
            dir_moved = (cursor[0]+dir[0], cursor[1]+dir[1])
            if 0<=dir_moved[0]<4 and 0<=dir_moved[1]<4:
                deq.append((board_str, dir_moved, cnt + 1, enter_pos))
        
        for dir in dirs:
            cntl_moved = cntl(board_str, cursor, dir)
            if cntl_moved[0] == cursor[0] and cntl_moved[1] == cursor[1]:
                continue
            else:
                deq.append((board_str, cntl_moved, cnt + 1, enter_pos))
        
        flip_pos = 4 * cursor[0] + cursor[1]
        if board_str[flip_pos] != 0:
            if enter_pos == -1:
                deq.append((board_str, cursor, cnt + 1, flip_pos))
            else:
                if enter_pos != flip_pos and board_str[enter_pos] == board_str[flip_pos]:
                    board_str = board_str.replace(board_str[flip_pos], "0")
                    deq.append((board_str, cursor, cnt + 1, -1))
                    
                    
'''
from itertools import permutations
from collections import deque

def ctrl(board, x0, y0, dx, dy):
    for i in range(1, 4):
        if 0 <= (x1 := x0 + dx * i) < 4 and 0 <= (y1 := y0 + dy * i) < 4:
            if board[x1][y1] > 0:
                return (x1, y1)
            l = i
    return (x0 + dx * l, y0 + dy * l)

def move(board, xy0, xy1):
    dist = [[6] * 4 for _ in range(4)]
    q = deque([(xy0, 0)])
    while q:
        [x, y], d = q.popleft()
        if d < dist[x][y]:
            dist[x][y] = d
            for dx, dy in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
                if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                    q.append(((x + dx, y + dy), d + 1))
                    q.append((ctrl(board, x, y, dx, dy), d + 1))
    return dist[xy1[0]][xy1[1]]

def solution(board, r, c):
    loc = {k: [] for k in range(1, 7)}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                loc[board[i][j]].append((i, j))
    minv = 100
    for p in permutations(filter(lambda v: v, loc.values())):
        sumv = 0
        xys = [(r, c)]
        stage = [[v for v in w] for w in board]
        for xy1, xy2 in p:
            vs = [(move(stage, xy, xy1) + move(stage, xy1, xy2), xy2) for xy in xys]\
               + [(move(stage, xy, xy2) + move(stage, xy2, xy1), xy1) for xy in xys]
            stage[xy1[0]][xy1[1]] = stage[xy2[0]][xy2[1]] = 0
            sumv += 2 + (mvn := min(vs)[0])
            xys = [xy for m, xy in vs if m == mvn]
        minv = min(sumv, minv)
    return minv
'''

if __name__ == "__main__":
    board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r = 1
    c = 0
    print(solution(board, r, c))
    # 14
    
    # board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
    # r = 0
    # c = 1
    # print(solution(board, r, c))
    # # 16