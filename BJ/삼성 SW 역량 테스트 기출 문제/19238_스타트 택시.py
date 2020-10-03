import sys
sys.stdin = open("19238_스타트 택시.txt", "r")

from collections import deque

def take_taxi(input_taxi):
    global map_data, taxi
    map_data[taxi[0]][taxi[1]] = 0

    deq = deque()
    deq.append(input_taxi)

    visited = []
    dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))
    while deq:
        temp_x, temp_y = deq.popleft()
        if type(map_data[temp_x][temp_y]) == list:
            taxi = [temp_x, temp_y]
            result = [0, map_data[temp_x][temp_y]]
            map_data[temp_x][temp_y] = 0
            return result

        for d in dirs:
            test_x, test_y = temp_x + d[0], temp_y + d[1]
            if 0<=test_x<N and 0<=test_y<N and map_data[test_x][test_y] != -1:
                if type(map_data[test_x][test_y]) == list:
                    taxi = [test_x, test_y]
                    result = [map_data[temp_x][temp_y] + 1, map_data[test_x][test_y]]
                    map_data[test_x][test_y] = 0
                    return result
                else:
                    test = [test_x, test_y]
                    if test not in visited:
                        visited.append(test)
                        map_data[test_x][test_y]=map_data[temp_x][temp_y] + 1
                        deq.append(test)
    return -1


def ride_taxi(input_taxi, input_destination):
    global map_data, taxi
    map_data[input_taxi[0]][input_taxi[1]] = 0

    if input_taxi == input_destination:
        taxi = input_destination
        return 0

    deq = deque()
    deq.append(input_taxi)

    visited = []
    recover = []
    dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))
    while deq:
        temp_x, temp_y = deq.popleft()
        for d in dirs:
            test_x, test_y = temp_x + d[0], temp_y + d[1]
            if 0<=test_x<N and 0<=test_y<N and map_data[test_x][test_y] != -1:
                if [test_x, test_y] == input_destination:
                    for r in recover:
                        map_data[r[0]][r[1]] = r[2:]
                    taxi = input_destination
                    return map_data[temp_x][temp_y] + 1
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
taxi = list(map(lambda x: x-1 ,map(int, input().split())))
passenger_data = [list(map(lambda x: x-1 ,map(int, input().split()))) for _ in range(M)]
for p_data in passenger_data:
    map_data[p_data[0]][p_data[1]] = p_data[2:]

flag, is_arrived = False, 0
while is_arrived != M:
    passenger = take_taxi(taxi)
    if passenger == -1 or fuel < passenger[0]:
        flag = True
        break
    else:
        distance, destination = passenger[0], passenger[1]
        fuel -= distance
    
        lets_ride = ride_taxi(taxi, destination)
        if lets_ride == -1 or fuel < lets_ride:
            flag = True
            break
        else:
            distance = lets_ride
            fuel += distance
            is_arrived += 1

if flag == True:
    print(-1)
else:
    print(fuel)
