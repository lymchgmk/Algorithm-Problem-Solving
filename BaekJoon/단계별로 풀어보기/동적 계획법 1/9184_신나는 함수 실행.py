import sys
sys.stdin = open("9184_신나는 함수 실행.txt", 'rt')


input = lambda: sys.stdin.readline().strip()


dp = [[[0]*21 for _ in range(21)] for _ in range(21)]


def func_w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return func_w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = func_w(a, b, c-1) + func_w(a, b-1, c-1) - func_w(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c] = func_w(a-1, b, c) + func_w(a-1, b-1, c) + func_w(a-1, b, c-1) - func_w(a-1, b-1, c-1)
    return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {func_w(a, b, c)}')