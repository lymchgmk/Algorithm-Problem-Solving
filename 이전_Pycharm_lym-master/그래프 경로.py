import sys
sys.stdin = open("그래프 경로.txt", "r")

def DFS(start):
    global result
    visited[start] = 1
    for next in range(1, v+1):
        if MyMap[start][next] and not visited[next]:
            if next == end_node:
                result = 1
                return
            DFS(next)

TC = int(input())
for tc in range(1, TC+1):
    v, e = map(int, input().split())
    MyMap = [[0]*(v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1

    start_node, end_node = map(int, input().split())
    result = 0
    DFS(start_node)
    print(f'#{tc} {result}')