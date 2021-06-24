import sys
sys.stdin = open("BJ_17471_게리맨더링.txt")

def dfs(graph, start_node):
    visit = []
    stack = []

    stack.append(start_node)

    while stack:
        temp = stack.pop()
        if temp not in visit:
            visit.append(temp)
            for i in range(1, N+1):
                if graph[temp][i] == 1:
                    stack.append(i)

    return visit

def powerset_garry(s):
    result = []
    for i in range(1<<len(s)):
        temp1 = [s[j] for j in range(len(s)) if i&(1<<j)]
        temp2 = list(set(list(range(1, N+1))) - set(temp1))
        if len(set(temp1)) >= 1 and len(temp2) >= 1 and len(temp1) >= len(temp2):
            result.append(temp1)
            result.append(temp2)
    return result

def garrymandering(garry):
    sum_list = []
    for i in range(0, len(garry), 2):
        sample1 = garry[i]
        sample2 = garry[i + 1]

        sample1_matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for x in sample1:
            for y in sample1:
                sample1_matrix[x][y] = adj_matrix[x][y]

        sample2_matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for x in sample2:
            for y in sample2:
                sample2_matrix[x][y] = adj_matrix[x][y]

        if len(sample1) == len(dfs(sample1_matrix, sample1[0])) and (len(sample2) == len(dfs(sample2_matrix, sample2[0]))):
            sum1 = 0
            for idx in sample1:
                sum1 += population[idx]
            sum2 = 0
            for idx in sample2:
                sum2 += population[idx]
            sum_list.append(abs(sum1 - sum2))

        else:
            continue

    if len(sum_list) == 0:
        return -1

    return min(sum_list)

N = int(input())
population = [0] + list(map(int, input().split()))
adj_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
V_list = [[0] for _ in range(N+1)]

idx = 1
for N_case in range(N):
    V = list(map(int, input().split()))
    V_list[idx] = V[1:]
    for i in range(1, V[0]+1):
        adj_matrix[idx][V[i]] = 1
        adj_matrix[V[i]][idx] = 1
    idx += 1

garry = powerset_garry(list(range(1, N+1)))

print(garrymandering(garry))