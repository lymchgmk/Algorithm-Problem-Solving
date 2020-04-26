import sys
sys.stdin = open('5122.수열편집.txt')

def edit(seq, data):
    if data[0] == 'I':
        seq.insert(int(data[1]), int(data[2]))
    elif data[0] == 'D':
        seq.pop(int(data[1]))
    elif data[0] == 'C':
        seq[int(data[1])]=int(data[2])
    return seq

T=int(input())

for test_case in range(1, T+1):
    N, M, L=map(int, input().split())
    seq_origin=list(map(int, input().split()))
    ans=0

    for i in range(M):
        seq_data=list(input().split())
        result=edit(seq_origin, seq_data)

    if len(result) < L:
        ans=-1
    else:
        ans=result[L]

    print(f'#{test_case} {ans}')