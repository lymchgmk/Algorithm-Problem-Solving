def solution(money, costs):
    values = [1, 5, 10, 50, 100, 500]
    coins = list(zip(values, costs))

    dp = [0] + [float('inf')] * money
    for value, cost in coins:
        for curr_money in range(money+1):
            dp[curr_money] = min(dp[curr_money], dp[curr_money - value] + cost)
    return dp[money]


if __name__ == "__main__":
    # tc 1
    # money = 4578
    # costs =	[1, 4, 99, 35, 50, 1000]
    # print(solution(money, costs))

    # tc 2
    money = 1999
    costs =	[2, 11, 20, 100, 200, 600]
    print(solution(money, costs))
    # int(input())
    # map(int, input().split())
    # list(map(int, input().split()))
    # solution()