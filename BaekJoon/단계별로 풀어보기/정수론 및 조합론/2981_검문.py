import sys
sys.stdin = open('2981_검문.txt', 'rt')


def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N = int(sys.stdin.readline())
N_list = sorted([int(sys.stdin.readline()) for _ in range(N)])
arr = []
for i in range(1, N):
    arr.append(N_list[i] - N_list[i-1])

GCD_arr = arr[0]
for i in range(N-1):
    GCD_arr = GCD(GCD_arr, arr[i])

result = []
result_rev = []
for i in range(1, int((GCD_arr)**0.5) + 1):
    if GCD_arr % i == 0:
        if i**2 == GCD_arr:
            result.append(i)
        else:
            result.append(i)
            result_rev.append(GCD_arr//i)

result = result[1:] + result_rev[::-1]
print(*result)


