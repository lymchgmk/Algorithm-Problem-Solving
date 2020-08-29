def air_condition(T):
# 1: 확산 후 배열 구하기
for i in range(R):
    for j in range(C):
        # 델타를 쓰자
        for dir in range(4):
            test_x = x + dx[i]
            test_y = y + dy[i]
            if (test_x == 0 or test_x == R or test_y == 0 or test_y == C) and
        # count = 4
        # if not 0 <= i-1 < R: count -= 1
        # elif not 0 <= i+1 < R: count -= 1
        # elif not 0 <= j-1 < C: count -= 1
        # elif not 0 <= j+1 < C: count -= 1

# 2: 공기청정기 돌리기

# 3: for 문으로 T번 하기
# 4: sum으로 먼지 모아서 카운트

R, C, T = map(int, input().split())

A_rc = [list(map(int, input().split())) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x, y = 0

