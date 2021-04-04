import sys
sys.stdin = open('1.txt', 'r')

n = 45
r = ''

while n:
    x, y = n//3, n%3
    r += str(y)
    n = x

ans = 0
test = list(map(int, r))[::-1]
for idx, t in enumerate(test):
    ans += ((3 ** idx) * t)
