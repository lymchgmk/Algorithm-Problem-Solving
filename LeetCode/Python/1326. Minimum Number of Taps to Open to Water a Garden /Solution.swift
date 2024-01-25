class Solution {
    func minTaps(_ n: Int, _ ranges: [Int]) -> Int {
        var dp = Array(repeating: n + 2, count: n + 1)
        dp[0] = 0

        for (i, r) in ranges.enumerated() {
            let (start, end) = (max(0, i - r), min(n, i + r))

            for j in (start...end) {
                dp[j] = min(dp[j], dp[start] + 1)
            }
        }

        return n + 2 <= dp[n] ? -1 : dp[n]
    }
}