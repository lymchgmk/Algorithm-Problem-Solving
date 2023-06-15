def solution(money):
    dp1 = [0] * len(money)
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    dp2 = [0] * len(money)
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1), max(dp2))


if __name__ == "__main__":
    money = [1, 2, 3, 1]
    result = 4
    answer = solution(money)
    print(answer == result, answer)
