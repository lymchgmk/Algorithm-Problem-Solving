MAX = 100_000
DIV = 1_000_000_007


def solution(n):
    dp = [0] * (MAX + 1)
    dp[1], dp[2], dp[3] = 1, 3, 10


if __name__ == "__main__":
    n = 3
    result = 10
    answer = solution(n)
    print(answer == result, answer)
