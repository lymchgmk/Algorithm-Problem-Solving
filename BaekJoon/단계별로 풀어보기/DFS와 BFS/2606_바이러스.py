import sys
sys.stdin = open('2606_바이러스.txt', 'rt')


def DFS(start):
    global DFS_result
    DFS_result.append(start)

    for next in adj_list[start]:
        if next not in DFS_result:
            DFS(next)


computers = int(input())
connected = int(input())
adj_list = [[] for _ in range(computers+1)]
for _ in range(connected):
    S, E = map(int, input().split())
    adj_list[S].append(E)
    adj_list[E].append(S)

DFS_result = []
DFS(1)
print(len(DFS_result)-1)