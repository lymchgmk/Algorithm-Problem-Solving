from collections import defaultdict


def solution(land, height):
    def DFS(land, height):
        marked = [[0] * N for _ in range(N)]
        marking = 1
        for start_x in range(N):
            for start_y in range(N):
                if marked[start_x][start_y] == 0:
                    stack = [(start_x, start_y, land[start_x][start_y])]
                    marked[start_x][start_y] = marking
                    while stack:
                        curr_x, curr_y, curr_h = stack.pop()
                        for dir_x, dir_y in dirs:
                            post_x, post_y = curr_x + dir_x, curr_y + dir_y
                            if 0 <= post_x < N and 0 <= post_y < N and marked[post_x][post_y] == 0:
                                post_h = land[post_x][post_y]
                                if abs(curr_h - post_h) <= height:
                                    stack.append((post_x, post_y, post_h))
                                    marked[post_x][post_y] = marking
                    marking += 1
        return marking, marked
    
    def install_ladders(land, marked):
        ladders = defaultdict(int)
        for curr_x in range(N):
            for curr_y in range(N):
                curr_h, curr_m = land[curr_x][curr_y], marked[curr_x][curr_y]
                for dir_x, dir_y in dirs:
                    post_x, post_y = curr_x + dir_x, curr_y + dir_y
                    if 0 <= post_x < N and 0 <= post_y < N:
                        post_h, post_m = land[post_x][post_y], marked[post_x][post_y]
                        if curr_m != post_m:
                            if ladders[(curr_m, post_m)] == 0:
                                ladders[(curr_m, post_m)] = abs(curr_h - post_h)
                            else:
                                ladders[(curr_m, post_m)] = min(ladders[(curr_m, post_m)], abs(curr_h - post_h))
        return ladders
    
    def MST(V, ladders):
        V -= 1
        adj = [[0] * V for _ in range(V)]
        for (s, e), c in ladders.items():
            adj[s-1][e-1] = c
            adj[e-1][s-1] = c
    
        INF = float('inf')
        key = [INF] * V
        p = [-1] * V
        mst = [False] * V
    
        key[0] = 0
        cnt = 0
        result = 0
        while cnt < V:
            min = INF
            u = -1
            for i in range(V):
                if not mst[i] and key[i] < min:
                    min = key[i]
                    u = i
        
            mst[u] = True
            result += min
            cnt += 1
        
            for w in range(V):
                if 0 < adj[u][w] < key[w] and not mst[w]:
                    key[w] = adj[u][w]
                    p[w] = u
        return result
        
    N = len(land)
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    marking, marked = DFS(land, height)
    ladders = install_ladders(land, marked)
    return MST(marking, ladders)


if __name__ == "__main__":
    land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
    height = 3
    print(solution(land, height)) # 15
    
    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    height = 1
    print(solution(land, height)) # 18
