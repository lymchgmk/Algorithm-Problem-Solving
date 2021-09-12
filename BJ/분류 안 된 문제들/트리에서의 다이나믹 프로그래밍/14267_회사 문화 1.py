import sys
sys.stdin = open("14267_회사 문화 1.txt", "r")
input = lambda: sys.stdin.readline().strip()


n, m = map(int, input().split())
tree = {idx: [] for idx in range(1, n+1)}
bosses = list(map(int, input().split()))
for man, boss in enumerate(bosses, start=1):
    if boss == -1:
        continue
    tree[boss].append(man)

dp = {idx: 0 for idx in tree}
for _ in range(m):
    i, w = map(int, input().split())
    dp[i] += w

stack = [1]
while stack:
    boss = stack.pop()
    for man in tree[boss]:
        dp[man] += dp[boss]
        stack.append(man)

print(*dp.values())
