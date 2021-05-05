def solution(arr):
    L = len(arr)
    N = L // 2 + 1
    dp_max = [[float('-inf')] * N for _ in range(N)]
    dp_min = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        dp_max[i][i] = int(arr[i * 2])
        dp_min[i][i] = int(arr[i * 2])

    for c in range(1, N):
        for i in range(N - c):
            j = c + i
            for k in range(j - i):
                if arr[2 * (i + k) + 1] == '-':
                    dp_max[i][j] = max(dp_max[i][i + k] - dp_min[i + k + 1][j], dp_max[i][j])
                    dp_min[i][j] = min(dp_min[i][i + k] - dp_min[i + k + 1][j], dp_min[i][j])
                elif arr[2 * (i + k) + 1] == '+':
                    dp_max[i][j] = max(dp_max[i][i + k] + dp_max[i + k + 1][j], dp_max[i][j])
                    dp_min[i][j] = min(dp_min[i][i + k] + dp_min[i + k + 1][j], dp_min[i][j])
    return dp_max[0][N - 1]