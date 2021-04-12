def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    dp = [[0, 0] for _ in range(len(sticker))]
    dp[0][0] = dp[1][0] = sticker[0]
    dp[1][1] = sticker[1]
    for i in range(2, len(sticker)-1):
        dp[i][0] = max(dp[i-1][0], dp[i-2][0] + sticker[i])
    for j in range(2, len(sticker)):
        dp[j][1] = max(dp[j-1][1], dp[j-2][1] + sticker[j])
    return max(dp[-2][0], dp[-1][1])


sticker1 = [14, 6, 5, 11, 3, 9, 2, 10]
sticker2 = [1, 3, 2, 5, 4]
sticker = sticker1
print(solution(sticker))
