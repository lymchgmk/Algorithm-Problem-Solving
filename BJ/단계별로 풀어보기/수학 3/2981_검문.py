import sys
sys.stdin = open('2981_검문.txt', 'rt')


N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
print(numbers)

for i in range(1, N):
    numbers[i] -= numbers[0]
numbers[0] = 0
print(numbers)