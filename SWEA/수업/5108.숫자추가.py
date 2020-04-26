import sys
sys.stdin = open('5108.숫자추가.txt')

T=int(input())

for test_case in range(1, 1+T):
    N, M, L = map(int, input().split())
    seq=list(map(int, input().split()))

    for _ in range(M):
        idx, val = map(int, input().split())
        seq.insert(idx, val)

    ans=seq[L]
    print(f'#{test_case} {ans}')