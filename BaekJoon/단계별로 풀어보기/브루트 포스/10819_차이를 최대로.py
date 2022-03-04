import sys
from itertools import permutations
sys.stdin = open('10819_차이를 최대로.txt', 'rt')


def solution(N, arr):
    def calc(_arr):
        return sum([abs(_arr[i] - _arr[i+1]) for i in range(N-1)])

    ans = 0
    for _arr in permutations(arr):
        ans = max(ans, calc(_arr))
    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    print(solution(N, arr))
