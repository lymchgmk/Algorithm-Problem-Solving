import sys
sys.stdin = open("5209_최소 생산 비용.txt")

def dfs(Vij, factory_idx, sum, visited):
    global result

    if factory_idx == N: # 종료조건
        if sum < result:
            result = sum
        return
    else:
        for product_idx in range(N):
            if visited[product_idx] == 0 and sum < result:  # sum < result 로 가지치기(이미 답이 될 가능성이 없는 경우)
                visited[product_idx] = 1
                dfs(Vij, factory_idx+1, sum + Vij[factory_idx][product_idx], visited) # visited[product_idx] = 1 이 된 상태에서 재귀로 다시 dfs
                visited[product_idx] = 0 # 다른 product_id에 대해 같은 깊이에서의 dfs를 해야하니까


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    Vij=[list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    result = 15*99 # 3<=N<=15, 1<=Vij<=99
    dfs(Vij, 0, 0, visited)

    print(f'#{test_case} {result}')