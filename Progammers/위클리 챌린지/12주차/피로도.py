from collections import deque


def solution(k, dungeons):
    L = len(dungeons)
    visited = [False] * L
    deq = deque()
    deq.append([k, visited])
    result = 0
    while deq:
        tmp_k, tmp_visited = deq.popleft()
        for i in range(L):
            req_k, cost = dungeons[i]
            if not tmp_visited[i] and tmp_k >= req_k and tmp_k - cost >= 1:
                tmp_visited[i] = True
                deq.append([tmp_k - cost, tmp_visited])
            else:
                result = max(result, len(tmp_visited))
    return result


if __name__ == "__main__":
    # tc 1
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    # ans 3
    print(solution(k, dungeons))
