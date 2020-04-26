import sys
sys.stdin = open("5099.피자굽기.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sample_list = list(map(int, input().split()))
    count = 0

    while count < M:
        sample_list.append(sample_list.pop(0))
        count += 1

    print(f'#{test_case} {sample_list[0]}')