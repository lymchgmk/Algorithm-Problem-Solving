def solution(n, tops):
    DIVIDER = 10007
    BASE = [[2, 1]] if tops[0] == 0 else [[3, 1]]
    dp = BASE + [[0, 0] for _ in range(n - 1)]

    for i in range(1, n):
        if tops[i] == 0:
            tri, dia = dp[i - 1]
            dp[i] = [(tri + dia + tri) % DIVIDER, (tri + dia) % DIVIDER]
        elif tops[i] == 1:
            tri, dia = dp[i - 1]
            dp[i] = [((tri + dia) * 2 + tri) % DIVIDER, (tri + dia) % DIVIDER]

    return sum(dp[-1]) % DIVIDER