import sys
sys.stdin = open('1541_잃어버린 괄호.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N = [n for n in input().split('-')]
for i in range(len(N)):
    if '+' in N[i]:
        N[i] = sum(map(int, N[i].split('+')))

answer = int(N[0])
for i in range(1, len(N)):
    answer -= int(N[i])
print(answer)
