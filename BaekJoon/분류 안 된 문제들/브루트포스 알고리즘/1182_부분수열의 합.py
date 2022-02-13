import sys
from itertools import combinations
sys.stdin = open("1182_부분수열의 합.txt", "rt")


def solution(N, S, nums):
    cnt = 0
    for size in range(1, N+1):
        for comb in combinations(nums, size):
            if sum(comb) == S:
                cnt += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.readline
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solution(N, S, nums))
