import sys
sys.stdin = open("2098_외판원 순회.txt", "rt")
input = lambda: sys.stdin.readline().strip()

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
dp = [[None]*(1<<N) for _ in range(N)]


def find_path(last, visited):
    VISITED_ALL = (1<<N) - 1
    if visited == VISITED_ALL:
        return W[last][0] or INF
    
    if dp[last][visited] is not None:
        return dp[last][visited]
    
    tmp = INF
    for city in range(N):
        if visited & (1 << city) == 0 and W[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])
    dp[last][visited] = tmp

    return tmp


print(find_path(0, 1<<0))

'''
def TSP_dp(dists):
    N = len(dists)
    VISITED_ALL = (1<<N) - 1
    cache = [[None]*(1<<N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF
        
        if cache[last][visited] is not None:
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])
        cache[last][visited] = tmp
        return tmp
    
    return find_path(0, 1 << 0)
'''
