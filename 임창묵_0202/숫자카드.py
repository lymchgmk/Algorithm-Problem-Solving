import sys
sys.stdin = open('숫자카드.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))
    count_0to9 = [0 for _ in range(10)]

    for i in range(len(ai)):
        count_0to9[ai[i]] += 1

    max_idx = 0
    max_count = 0
    for i in range(len(count_0to9) -1, -1, -1):
        if count_0to9[i] > max_idx:
            max_idx = count_0to9[i]
            max_count = i

    print(f'#{test_case} {max_count} {max_idx}')