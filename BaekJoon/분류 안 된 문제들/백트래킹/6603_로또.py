import sys
from itertools import combinations
sys.stdin = open("6603_로또.txt", "rt")


def solution(k, S):
    SIZE = 6
    for comb in combinations(S, SIZE):
        print(*comb)
    print()

if __name__ == "__main__":
    input = sys.stdin.readline
    while True:
        k, *S = map(int, input().split())
        if k == 0:
            break
        solution(k, S)
