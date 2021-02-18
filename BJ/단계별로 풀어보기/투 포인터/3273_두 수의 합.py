import sys
sys.stdin = open('3273_두 수의 합.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

l, r = 0, n-1
ans = 0
while l < r:
    temp = a[l] + a[r]
    if temp == x:
        ans += 1
    if temp < x:
        l += 1
        continue
    r -= 1
print(ans)