import sys
from copy import deepcopy
sys.stdin=open("14503_로봇 청소기.txt")

def clean(loc):
    global my_room
    if my_room[loc[0]][loc[1]] == 0:
        my_room[loc[0]][loc[1]] = 1
        return 1
    else:
        return 0

def search(current_loc, current_dir_idx):
    for i in range(1, 5):
        next_dir_idx=(current_dir_idx+i)%4
        next_dir=dirs[next_dir_idx]
        next_loc=[current_loc[0]+next_dir[0], current_loc[1]+next_dir[1]]

        if my_room[next_loc[0]][next_loc[1]] == 0:
            return [next_loc, next_dir_idx]

    return False

def robot(start_loc, start_dir_idx):
    global my_room, count

    for x in my_room:
        print(x)

    print('------------------------')

    count+=clean(start_loc)

    temp=search(start_loc, start_dir_idx)
    if temp:
        robot(temp[0], temp[1])
    else:
        back_dir_idx = (start_dir_idx + 2) % 4
        back_dir = dirs[back_dir_idx]
        back_loc = [start_loc[0] + back_dir[0], start_loc[1] + back_dir[1]]
        if my_room[back_loc[0]][back_loc[1]] == 1:
            return
        else:
            robot(back_loc, start_dir_idx)


N, M = map(int, input().split())
start_status=list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(N)]

my_room=deepcopy(data)

count=0

dirs=((-1, 0),(0, -1),(1, 0),(0, 1)) # 북 서 남 동

robot([start_status[0], start_status[1]], start_status[2])

print(count)


