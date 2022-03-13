from collections import defaultdict


def solution(n, edges):
    def dfs(start, visited, path):



    adj = {i: [] for i in range(n)}
    for s, e in edges:
        adj[s].append(e)
        adj[e].append(s)

    routes = set()
    for start in range(n):
        visited = [False] * n
        path = []
        dfs(start, str(start))


if __name__ == "__main__":
    # tc 1
    n = 5
    edges = [[0,1],[0,2],[1,3],[1,4]]
    print(solution(n, edges))

    # tc 2
    # n = 4
    # edges = [[2,3],[0,1],[1,2]]
    # print(solution(n, edges))
