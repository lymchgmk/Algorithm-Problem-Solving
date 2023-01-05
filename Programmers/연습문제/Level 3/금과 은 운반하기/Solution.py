def solution(a, b, g, s, w, t):
    left, right = 1, 4 * (10 ** 14)
    cities = range(len(t))

    while left <= right:
        mid = (left + right) // 2
        W, G, S = 0, 0, 0
        for city in cities:
            if mid < t[city]:
                continue

            loads = (1 + (mid - t[city]) // (t[city] * 2)) * w[city]
            G += min(loads, g[city])
            S += min(loads, s[city])
            W += min(loads, g[city] + s[city])

        if a <= G and b <= S and (a + b) <= W:
            right = mid - 1
        else:
            left = mid + 1

    return left