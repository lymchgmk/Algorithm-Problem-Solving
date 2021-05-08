from collections import deque


def corona_check(waiting_room, x, y):
    deq = deque([[x, y, True]])
    cnt = 2
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = [[False] * 5 for _ in range(5)]
    while cnt:
        tmp = deque()
        while deq:
            curr_x, curr_y, status = deq.popleft()
            visited[curr_x][curr_y] = True
            for dir_x, dir_y in dirs:
                post_x, post_y = curr_x + dir_x, curr_y + dir_y
                if 0 <= post_x < 5 and 0 <= post_y < 5 and not visited[post_x][post_y]:
                    if waiting_room[post_x][post_y] == 'P':
                        if status:
                            return False
                        else:
                            tmp.append([post_x, post_y, True])
                    elif waiting_room[post_x][post_y] == 'X':
                        tmp.append([post_x, post_y, False])
                    else:
                        tmp.append([post_x, post_y, status])
        deq, tmp = tmp, deque()
        cnt -= 1
    return True


place = ["PXPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]
print(1, 1, corona_check(place, 1, 1))
