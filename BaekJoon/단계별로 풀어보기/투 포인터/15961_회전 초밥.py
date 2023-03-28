.import sys
from collections import Counter
sys.stdin = open("15961_회전 초밥.txt", 'rt')


def solution(N, D, K, C, sushi):
    answer = 0
    sushi += sushi[:K-1]
    cntr = Counter(sushi[:K])
    cntr[C] += 1
    for left in range(N-1):
        right = left + K
        cntr[sushi[left]] -= 1
        if cntr[sushi[left]] == 0:
            del cntr[sushi[left]]
        cntr[sushi[right]] += 1
        answer = max(answer, len(cntr))
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    N, D, K, C = map(int, input().split())
    sushi = [int(input()) for _ in range(N)]
    print(solution(N, D, K, C, sushi))
