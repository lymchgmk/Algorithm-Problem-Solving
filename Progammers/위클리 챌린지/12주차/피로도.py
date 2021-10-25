from collections import deque, defaultdict


def solution(k, dungeons):
    L = len(dungeons)
    visited = defaultdict(lambda: False)
    DP = deque([[k, visited]])
    result = 0
    while DP:
        tmp_k, tmp_visited = DP.popleft()
        for i in range(L):
            req, cost = dungeons[i]
            if not tmp_visited[i] and tmp_k >= req and tmp_k > cost:
                tmp_visited[i] = True
                DP.append([tmp_k - cost, tmp_visited])
            else:
                result = max(result, len(tmp_visited))
    return result


if __name__ == "__main__":
    # tc 1
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    # ans 3
    print(solution(k, dungeons))
