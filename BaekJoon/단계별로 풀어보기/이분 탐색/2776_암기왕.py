import sys
from bisect import bisect_left
sys.stdin = open('2776_암기왕.txt', 'rt')


def solution(N, M, note1, note2):
    note1.sort()
    for num in note2:
        idx = bisect_left(note1, num)
        if 0 <= idx < N and note1[idx] == num:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        note1 = list(map(int, input().split()))
        M = int(input())
        note2 = list(map(int, input().split()))
        solution(N, M, note1, note2)
