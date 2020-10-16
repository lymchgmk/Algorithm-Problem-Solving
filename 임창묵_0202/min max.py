import sys
sys.stdin = open('min max.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    print(f'#{test_case} {max(N_list)-min(N_list)}')