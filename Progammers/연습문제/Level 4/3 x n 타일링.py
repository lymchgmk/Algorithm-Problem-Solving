def solution(n):
    if n % 2 == 1:
        return 0
    
    dp = [0] * (n+1)
    dp[0] = 1
    prev = 0
    for i in range(2, n+1, 2):
        dp[i] = (3*dp[i-2] + 2*prev) % 1000000007
        prev += dp[i-2]
    
    return dp[n]


'''
def solution(n):
    if n % 2:
        return 0
    front = back = 1
    for _ in range(n//2):
        front, back = back, (4*back - front) % 1000000007
    return back
'''