import sys
sys.stdin=open("5189_전기카트.txt")
from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    NxN = [list(map(int, input().split())) for _ in range(N)]

    answer = 10000
    routes = permutations(range(1, N))
    for route in routes:
        result = 0
        way = [0] + list(route) + [0]
        for idx in range(len(way)-1):
            result += NxN[way[idx]][way[idx + 1]]
        if result < answer:
            answer = result

    print(f'#{test_case} {answer}')