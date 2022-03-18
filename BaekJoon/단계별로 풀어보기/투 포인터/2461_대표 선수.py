import heapq
import sys
import os
file_name = os.path.basename(sys.argv[0])[:-3] + ".txt"
sys.stdin = open(file_name, "rt")


def solution(N, M, students):
    hp = []
    for idx, student in enumerate(students):
        val = heapq.heappop(student)
        heapq.heappush(hp, (val, idx))

    min_val, max_val = 1e9, 0
    for _val, _ in hp:
        min_val = min(min_val, _val)
        max_val = max(max_val, _val)
    diff = max_val - min_val

    while hp:
        curr_val, min_idx = heapq.heappop(hp)
        if not students[min_idx]:
            break
        else:
            post_val = heapq.heappop(students[min_idx])
            heapq.heappush(hp, (post_val, min_idx))

        min_val = hp[0][0]
        max_val = max(max_val, post_val)
        diff = min(diff, max_val - min_val)
    return diff


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N, M = map(int, input().split())
    students = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        heapq.heapify(tmp)
        students.append(tmp)
    print(solution(N, M, students))
