import sys
import heapq


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N = int(input())
    hq = []
    for _ in range(N):
        S, F = map(int, input().split())
        heapq.heappush(hq, (F, S))

    curr_time = 0
    count = 0
    while hq:
        end_time, start_time = heapq.heappop(hq)
        if curr_time <= start_time:
            curr_time = end_time
            count += 1

    print(count)
