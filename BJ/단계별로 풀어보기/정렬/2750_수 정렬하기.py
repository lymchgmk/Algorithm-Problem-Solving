import sys
sys.stdin = open('2750_수 정렬하기.txt', 'rt')

N = int(input())
numbers = [int(input()) for _ in range(N)]
for n in sorted(numbers):
    print(n)