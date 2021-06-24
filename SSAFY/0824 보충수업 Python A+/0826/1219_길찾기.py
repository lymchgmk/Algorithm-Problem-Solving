import sys
sys.stdin = open('1219_길찾기.txt', 'r')

# txtFile = open('1219_길찾기.txt', 'r')
# 
# while True:
#     line1 = txtFile.readline()
#     if line1 == '': break
#     line2 = txtFile.readline()
# 
#     test_case, road = map(int, line1.split())
#     start, end = [], []
#     for i in range(road):
#         start.append(line2)
# 
# txtFile.close()

def dfs(start, graph):
    stack = [start]
    visited = []

    while stack:
        temp = stack.pop()
        if temp not in visited:
            visited.append(temp)
            for node in graph[temp]:
                stack.append(node)

    return visited

for _ in range(10):
    start, end = 0, 99
    test_case, N = map(int, input().split())
    inputdata = list(map(int, input().split()))

    mydata = [[] for _ in range(100)]
    for i in range(N):
        mydata[inputdata[2*i]].append(inputdata[2*i+1])

    mypath = dfs(start, mydata)

    if end in mypath: result = 1
    else: result = 0

    print('#{} {}'.format(test_case, result))


    # def dfs(v):
    #     global res
    #     if v == 99:
    #         res = 1
    #         return
    #     else:
    #         for i in range(100):
    #             if board[v][i]:
    #                 board[v][i] = 0
    #                 dfs(i)
    #
    #
    # T = 10
    # for t in range(1, T + 1):
    #     n, m = map(int, input().split())
    #     numbers = list(map(int, input().split()))
    #     board = [[0] * (100) for _ in range(100)]
    #     res = 0
    #     for i in range(0, len(numbers), 2):
    #         board[numbers[i]][numbers[i + 1]] = 1
    #     dfs(0)
    #     print('#%d %d' % (t, res))

