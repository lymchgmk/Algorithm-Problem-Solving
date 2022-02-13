import sys
from collections import Counter
sys.stdin = open("1475_방 번호.txt", "rt")


def solution(N):
    cntr = Counter(N)
    tmp = (cntr['6'] + cntr['9'] + 1) // 2
    cntr['6'] = cntr['9'] = 0
    return max(cntr.most_common()[0][1], tmp)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = input()
    print(solution(N))
