from heapq import heappush, heappop


def solution(n, k, enemy):
    hq = []
    for round, monster in enumerate(enemy):
        heappush(hq, monster)
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return round

    return len(enemy)


if __name__ == "__main__":
    n = 7
    k = 3
    enemy = [4, 2, 4, 5, 3, 3, 1]
    print(solution(n, k, enemy))