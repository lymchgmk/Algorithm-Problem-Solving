import sys
sys.stdin = open("9370_미확인 도착지.txt", "rt")
input = lambda: sys.stdin.readline().strip()
import heapq


def dijkstra():
    pass


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    dist = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        adj

    for _ in range(t):
        x = int(input())

'''
import heapq
from math import inf
input = sys.stdin.readline

def candy(n, start, edges, targets): 
    distance = [inf] * (n + 1)
    distance[start] = 0
    que = [(0, start)]
    ans = []
    while que:
        d, p = heapq.heappop(que)
        if distance[p] < d:
            continue
            
        if p in targets: #목표 노드를 지나가게 되면
            targets.remove(p) #타겟 셋에서 후보 노드를 제외하고
            if d % 2: #가중치가 짝수인지 아닌지 비교한다.
                ans.append(p)
                if not targets: #타겟이 더 이상 없다면 
                    return sorted(ans) #정답을 정렬해서 반환한다.
                    
        for f in edges[p]:
            if d + edges[p][f] < distance[f]:
                distance[f] = d + edges[p][f]
                heapq.heappush(que, (distance[f], f))
    return sorted(ans)

tc = int(input())
for __ in range(tc):
    n, m, t = map(int, input().split()) 
    s, g, h = map(int, input().split())
    e = [{} for _ in range(n + 1)] # 가중치 값을 받는다.
    for _ in range(m):
        i, j, d = map(int, input().split())
        # 모든 가중치를 2배 해주고
        e[i][j] = 2 * d 
        e[j][i] = 2 * d
    # g에서 h로 가는 노드만 홀수로 만들어준다.
    e[g][h] -= 1
    e[h][g] -= 1
    
    #만약 s에서 t로 가는 최단 경로가 g와 h를 포함하는 경로를 포함해 1개 이상이라면 무조건 g와 h를 선택
    #뿐만 아니라 g와 h를 지나면 가중치 합이 무조건 홀수
    print(*candy(n, s, e, {int(input()) for _ in range(t)}))
'''