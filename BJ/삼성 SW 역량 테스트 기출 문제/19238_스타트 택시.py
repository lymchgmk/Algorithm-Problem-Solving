import sys
from collections import deque
sys.stdin = open("19238_스타트 택시.txt", "r")


def take_taxi(taxi_input):
    global map_data
    map_data[taxi_input[0]][taxi_input[1]] = 0

    deq = deque()
    deq.append(taxi_input)

    visited = [taxi_input]
    dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))
    while deq:
        print(deq)
        temp_x, temp_y = deq.popleft()
        if type(map_data[temp_x][temp_y]) == list:
            result = [temp_x, temp_y] + map_data[temp_x][temp_y]
            map_data[temp_x][temp_y] = 0
            return result

        for d in dirs:
            test_x, test_y = temp_x + d[0], temp_y + d[1]
            if 0 <= test_x < N and 0 <= test_y < N and map_data[test_x][test_y] != -1:
                if type(map_data[test_x][test_y]) == list:
                    result = [map_data[temp_x][temp_y] + 1] + [test_x, test_y] + map_data[test_x][test_y]
                    map_data[test_x][test_y] = 0
                    return result
                else:
                    test = [test_x, test_y]
                    if test not in visited:
                        visited.append(test)
                        map_data[test_x][test_y] = map_data[temp_x][temp_y] + 1
                        deq.append(test)
    return -1


def ride_taxi(taxi_input, destination_input):
    global map_data
    map_data[taxi_input[0]][taxi_input[1]] = 0

    if taxi_input == destination_input:
        return [0] + destination_input

    deq = deque()
    deq.append(taxi_input)

    visited = [taxi_input]
    recover = []
    dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))
    while deq:
        print(deq)
        temp_x, temp_y = deq.popleft()
        for d in dirs:
            test_x, test_y = temp_x + d[0], temp_y + d[1]
            if 0 <= test_x < N and 0 <= test_y < N and map_data[test_x][test_y] != -1:
                if [test_x, test_y] == destination_input:
                    for r in recover:
                        map_data[r[0]][r[1]] = r[2:]
                    return [map_data[temp_x][temp_y] + 1] + destination_input
                else:
                    if [test_x, test_y] not in visited:
                        visited.append([test_x, test_y])
                        if type(map_data[test_x][test_y]) == list:
                            recover.append([test_x, test_y] + map_data[test_x][test_y])
                        map_data[test_x][test_y] = map_data[temp_x][temp_y] + 1
                        deq.append([test_x, test_y])
    return -1


N, M, fuel = map(int, input().split())
map_data = [list(-x for x in map(int, input().split())) for _ in range(N)]
taxi = list(x-1 for x in map(int, input().split()))
passenger_data = [[x-1 for x in map(int, input().split())] for _ in range(M)]
for p_data in passenger_data:
    map_data[p_data[0]][p_data[1]] = p_data[2:]

flag, is_arrived = False, 0
while is_arrived != M:
    passenger = take_taxi(taxi)
    if passenger == -1 or fuel < passenger[0]:
        flag = True
        break
    else:
        distance, taxi, destination = passenger[0], passenger[1:3], passenger[3:]
        fuel -= distance

        lets_ride = ride_taxi(taxi, destination)
        if lets_ride == -1 or fuel < lets_ride[0]:
            flag = True
            break
        else:
            distance, taxi = lets_ride[0], lets_ride[1:]
            fuel += distance
            is_arrived += 1

if flag:
    print(-1)
else:
    print(fuel)
