import sys
sys.stdin = open('17298_오큰수.txt', 'rt')


N = int(input())
A = list(map(int, input().split()))
stack = []
NGE = [-1]*N
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)