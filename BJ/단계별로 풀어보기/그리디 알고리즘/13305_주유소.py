import sys
sys.stdin = open('13305_주유소.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
dist = list(map(int, input().split()))
price, *price_list = list(map(int, input().split()))

result = 0
for i in range(N-1):
    result += dist[i] * price
    price = min(price, price_list[i])

print(result)