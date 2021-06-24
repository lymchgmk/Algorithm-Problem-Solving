import sys
import collections

sys.stdin = open('2468_안전 영역.txt', 'rt', encoding='UTF8')

def bfs(G, v):
    visited = [0 for _ in range(V+1)]
    deq = collections.deque()

    deq.append(v)  #enQueue
    visited[v] = 1
    print(v, end=" ")
    while len(deq) != 0: # 아니면 그냥 while deq: 로도 가능, 어차피 비면 False
        v = deq.popleft() #deQueue
        for w in range(1, V+1):
            if G[v][w] == 1 and visited[w] == 0:
                deq.append(w)
                visited[w] = 1
                print(w, end=" ")

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)] #2차원 초기화

for i in range(0, len(temp), 2):  #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1):  #입력확인
    print("{} {}".format(i, G[i]))

bfs(G, 1)


#1. 물 높이(=h) 마다 h 초과인 지역을 NxN 매트릭스 만들기
#2. bfs 탐색으로 탐색 끝날 때 마다 count += 1
#3. (h, count) 기록
#4. h += 1 증가, count = 0 초기화
#5. 1 <= h <= 100 동안 계속
#6. max(count) 출력