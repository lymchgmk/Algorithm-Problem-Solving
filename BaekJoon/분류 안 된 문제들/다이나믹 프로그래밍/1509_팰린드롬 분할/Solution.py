import sys


def solution(word):
    dp = [[0] * len(word) for _ in range(len(word))]

    for i in range(len(word)):
        dp[0][i] = 1

    for row in dp:
        print(row)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()

    word = "ABACABA"
    solution(word)