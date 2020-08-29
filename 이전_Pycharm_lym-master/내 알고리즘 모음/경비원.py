def point(arr, store):
    p = store[-1]
    if store[0] == 1: #북
        arr[0][store[1]] = p
    if store[0] == 2: #남
        arr[-1][store[1]] = p
    if store[0] == 3: #서
        arr[store[1]][0] = p
    if store[0] == 4: #동
        arr[store[1]][-1] = p

def distance(N, M, stores_list, DG):
    result = 0
    for i in range(stores_num):
        if stores_list[i][-1] == DG[-1]:
            result += abs(stores_list[i][1] - DG[1])

        elif (stores_list[i][-1] != DG[-1]) and (DG[-1] in [1, 2]) and (stores_list[i][-1] in [1, 2]):
            result += min((DG[1] + stores_list[i][1]), 2*N - (DG[1] + stores_list[i][1])) + M
        elif (stores_list[i][-1] != DG[-1]) and (DG[-1] in [3, 4]) and (stores_list[i][-1] in [3, 4]):
            result += min((DG[1] + stores_list[i][1]), 2*M - (DG[1] + stores_list[i][1])) + N

        elif DG[-1] == 1 and stores_list[i][-1] == 3:
            result += (stores_list[i][1] + DG[1])
        elif DG[-1] == 1 and stores_list[i][-1] == 4:
            result += (stores_list[i][1] + (N - DG[1]))

        elif DG[-1] == 2 and stores_list[i][-1] == 3:
            result += ((M-stores_list[i][1]) + DG[1])
        elif DG[-1] == 2 and stores_list[i][-1] == 4:
            result += ((M-stores_list[i][1]) + (N-DG[1]))

        elif DG[-1] == 3 and stores_list[i][-1] == 1:
            result += (stores_list[i][1] + DG[1])
        elif DG[-1] == 3 and stores_list[i][-1] == 2:
            result += (stores_list[i][1] + (M - DG[1]))

        elif DG[-1] == 4 and stores_list[i][-1] == 1:
            result += ((N-stores_list[i][1]) + DG[1])
        elif DG[-1] == 4 and stores_list[i][-1] == 2:
            result += ((N-stores_list[i][1]) + (M - DG[1]))

    return result


N, M = map(int, input().split())  # N: 가로 / M: 세로
arr = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

stores_num = int(input())
stores_list = []
for stores in range(stores_num):
    store = list(map(int, input().split())) + [1]
    stores_list.append(store)
    point(arr, store)

DG = list(map(int, input().split())) + [2]
point(arr, DG)

print(distance(N, M, stores_list, DG))