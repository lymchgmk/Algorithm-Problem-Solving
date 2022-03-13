import sys
from collections import deque
sys.stdin = open("15961_회전 초밥.txt", 'rt')


def solution(N, D, K, C, sushi):
    answer = 0
    sushi = sushi + sushi[:K-1]
    left, right = 0, K
    window = deque(sushi[left: right])
    print(sushi)
    for i in range(N):
        print(sushi[i: i+K])


if __name__ == "__main__":
    input = sys.stdin.readline
    N, D, K, C = map(int, input().split())
    sushi = [int(input()) for _ in range(N)]
    print(solution(N, D, K, C, sushi))
