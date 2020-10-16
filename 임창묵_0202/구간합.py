import sys
sys.stdin = open('구간합.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))

    for i in range(len(v)-M+1):
        vv_list = [0 for _ in range(int(len(v)-M+1))]
        for j in range(len(vv_list)):
            vv_list[j] = sum(v[j:j+M])

    print(f'#{test_case} {max(vv_list)-min(vv_list)}')