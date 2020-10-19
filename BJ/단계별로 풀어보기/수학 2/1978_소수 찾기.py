import sys
sys.stdin = open('1978_소수 찾기.txt', 'rt')

N = int(input())
numbers = list(map(int, input().split()))

count = 0
for n in numbers:
    if n >= 2:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                break
        else:
            count += 1

print(count)
