import heapq


def solution(n, k, enemy):
    queue = []
    for round in range(len(enemy)):
        heapq.heappush(queue, enemy[round])

        if len(queue) > k:
            n -= heapq.heappop(queue)

        if n < 0:
            return round

    return len(enemy)


if __name__ == "__main__":
    n = 7
    k = 3
    enemy = [4, 2, 4, 5, 3, 3, 1]
    print(solution(n, k, enemy))