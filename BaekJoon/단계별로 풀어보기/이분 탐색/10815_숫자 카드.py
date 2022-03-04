import sys
from bisect import bisect_left
sys.stdin = open('10815_숫자 카드.txt', 'rt')


def solution(N, M, cards, nums):
    answer = [0]*M
    cards.sort()
    for idx, num in enumerate(nums):
        b_idx = bisect_left(cards, num)
        if 0 <= b_idx < N and cards[b_idx] == num:
            answer[idx] = 1
    print(*answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    nums = list(map(int, input().split()))
    solution(N, M, cards, nums)
