import sys
sys.stdin = open('10773_제로.txt', 'rt')


N = int(input())
stack = []
for _ in range(N):
    money = int(input())
    if money == 0:
        stack.pop()
    else:
        stack.append(money)

print(sum(stack))
