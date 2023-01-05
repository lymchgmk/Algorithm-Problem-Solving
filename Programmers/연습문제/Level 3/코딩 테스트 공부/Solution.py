def solution(alp, cop, problems):
    INF = float('inf')
    alp_req_max, cop_req_max = 0, 0
    for alp_req, cop_req, _, _, _ in problems:
        alp_req_max = max(alp_req_max, alp_req)
        cop_req_max = max(cop_req_max, cop_req)

    if alp_req_max <= alp and cop_req_max <= cop:
        return 0

    alp, cop = min(alp, alp_req_max), min(cop, cop_req_max)
    dp = [[INF] * (cop_req_max + 1) for _ in range(alp_req_max + 1)]
    dp[alp][cop] = 0
    for curr_alp in range(alp, alp_req_max + 1):
        for curr_cop in range(cop, cop_req_max + 1):
            if curr_alp < alp_req_max:
                dp[curr_alp + 1][curr_cop] = min(dp[curr_alp][curr_cop] + 1, dp[curr_alp + 1][curr_cop])
            if curr_cop < cop_req_max:
                dp[curr_alp][curr_cop + 1] = min(dp[curr_alp][curr_cop] + 1, dp[curr_alp][curr_cop + 1])

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= curr_alp and cop_req <= curr_cop:
                    post_alp = min(curr_alp + alp_rwd, alp_req_max)
                    post_cop = min(curr_cop + cop_rwd, cop_req_max)
                    dp[post_alp][post_cop] = min(dp[curr_alp][curr_cop] + cost, dp[post_alp][post_cop])

    return dp[alp_req_max][cop_req_max]