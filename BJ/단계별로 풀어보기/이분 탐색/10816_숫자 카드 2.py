import sys
sys.stdin = open("10816_숫자 카드 2.txt", 'rt')

from collections import Counter
input = lambda: sys.stdin.readline().strip()
_ = input()
N_list = input().split()
_ = input()
M_list = input().split()

C = Counter(N_list)
print(*list(C[m] if m in C else 0 for m in M_list))


res_dict = {}
for N in N_list:
    if N not in res_dict:
        res_dict[N] = 1
    else:
        res_dict[N] += 1

print(*list(res_dict[M] if M in res_dict else 0 for M in M_list))
