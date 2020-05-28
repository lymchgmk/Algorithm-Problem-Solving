import sys
sys.stdin=open("1247_최적 경로.txt")

from itertools import permutations

T=int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    coordinate = []
    for idx in range(N + 2):
        if idx == 0:
            company = (data[idx * 2], data[idx * 2 + 1])
            coordinate.append(company)
        elif idx == 1:
            home = (data[idx * 2], data[idx * 2 + 1])
        else:
            coordinate.append((data[idx * 2], data[idx * 2 + 1]))
    coordinate.append(home)

    result = float('inf')
    routes = permutations(range(1, N+1))

    for route in routes:
        route = list(route) + [N + 1]
        route_length = 0
        count = 0
        for i in range(len(route)):
            if route_length > result:
                break

            if count == 0:
                route_length += abs(coordinate[0][0] - coordinate[route[i]][0]) + abs(
                    coordinate[0][1] - coordinate[route[i]][1])
            elif count == N + 1:
                route_length += abs(coordinate[-1][0] - coordinate[route[i]][0]) + abs(
                    coordinate[-1][1] - coordinate[route[i]][1])
            else:
                route_length += abs(coordinate[route[i - 1]][0] - coordinate[route[i]][0]) + abs(
                    coordinate[route[i - 1]][1] - coordinate[route[i]][1])

            count += 1

        if route_length <= result:
            result = route_length

    print(f'#{test_case} {result}')