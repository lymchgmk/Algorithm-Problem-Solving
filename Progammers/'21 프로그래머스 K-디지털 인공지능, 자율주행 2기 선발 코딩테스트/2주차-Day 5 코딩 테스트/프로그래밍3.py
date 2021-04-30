def solution(strs, t):
    strs_dict = {s[0]: [] for s in strs}
    for s in strs:
        strs_dict[s[0]].append(s)
    
    L = len(t)
    INF = float('inf')
    dp = [0] + [INF] * L
    for i in range(1, L+1):
        j = i-5 if i > 5 else 0
        while j < i:
            if dp[j] + 1 < dp[i] and t[j:i] in strs_dict[t[j]]:
                dp[i] = dp[j] + 1
            j += 1
    
    return dp[-1] if dp[-1] != INF else -1
    
    
strs = ["ba", "na", "n", "a"]
t = "banana"
print(solution(strs, t))
