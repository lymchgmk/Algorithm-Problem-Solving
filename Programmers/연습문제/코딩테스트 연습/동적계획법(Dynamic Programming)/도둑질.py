def solution(money):
    dp = [0]*len(money)
    dp[0], dp[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
        
    dp2 = [0]*len(money)
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    return max(max(dp), max(dp2))


money = [1, 1, 4, 1, 4]
print(solution(money))