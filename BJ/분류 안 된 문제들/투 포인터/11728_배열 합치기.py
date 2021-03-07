import sys
sys.stdin = open('11728_배열 합치기.txt', 'r')


input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

start_A, start_B = 0, 0
result = []
while True:
    if start_A == N or start_B == M:
        if start_A != N:
            result += A[start_A:]
        if start_B != M:
            result += B[start_B:]
        break
    
    if A[start_A] < B[start_B]:
        result.append(A[start_A])
        start_A += 1
    elif A[start_A] > B[start_B]:
        result.append(B[start_B])
        start_B += 1
    else:
        result.append(A[start_A])
        result.append(B[start_B])
        start_A += 1
        start_B += 1
        
print(*result)