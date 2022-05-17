def solution(strs, t):
    L = len(t)
    strs_set = set(strs)
    dp = [0] + [float('inf')] * L
    for end in range(L):
        for start in range(max(0, end-5), end+1):
            if t[start:end+1] in strs_set:
                dp[end+1] = min(dp[end+1], dp[start] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1
    

strs = ["ba","na","n","a"]
t = 'banana'
print(solution(strs, t))
