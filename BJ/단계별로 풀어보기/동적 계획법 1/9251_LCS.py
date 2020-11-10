import sys
sys.stdin = open("9251_LCS.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
X = input()
Y = input()


def LCS_recursion(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + LCS_recursion(xs, ys)
    else:
        return max(LCS_recursion(xstr, ys), LCS_recursion(xs, ystr), key=len)


def LCS_DP(xstr, ystr):
    L = [[0]*(len(ystr)+1) for _ in range(len(xstr)+1)]
    for i, x in enumerate(xstr):
        for j, y in enumerate(ystr):
            if x == y:
                L[i+1][j+1] = L[i][j] + 1
            else:
                L[i+1][j+1] = max(L[i+1][j], L[i][j+1])

    result = ''
    j = len(ystr)
    for i in range(1, len(xstr)+1):
        if L[i][j] != L[i-1][j]:
            result += ystr[i-1]
    return result


print(len(LCS_recursion(X, Y)))
print(len(LCS_DP(X, Y)))