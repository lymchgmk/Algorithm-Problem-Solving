import sys
sys.stdin = open("2999_비밀 이메일.txt")

message = list(input())
N = len(message)
for i in range(int(N**0.5)+1, 0, -1):
    if N/i == int(N/i) and i <= int(N/i):
        R, C = i, int(N/i)
        break

decrypt_arr = [[[] for _ in range(R)] for _ in range(C)]
for i in range(N):
    x, y = i//R, i%R
    decrypt_arr[x][y] = message[i]

result = ''
for i in range(R):
    col = [col[i] for col in decrypt_arr]
    for c in col:
        result += c

print(result)