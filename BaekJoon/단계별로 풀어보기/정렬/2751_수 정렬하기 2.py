import sys
sys.stdin = open('2751_수 정렬하기 2.txt', 'rt')

N = int(input())
numbers = [int(input()) for _ in range(N)]
for n in sorted(numbers):
    print(n)