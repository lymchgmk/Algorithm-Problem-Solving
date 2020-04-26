import sys
sys.stdin = open('5178.노드의합.txt')

T=int(input())

for test_case in range(1, T+1):
    N,M,L=map(int, input().split())

    for i in range(10):
        if 2**i<=N<2**(i+1):
            cnt=i
            break

    tree=[0]*(2**(cnt+1))
    for i in range(M):
        data=list(map(int, input().split()))
        tree[data[0]]=data[1]

    stack=[L]
    result=[]

    while True:
        while stack:
            temp=stack.pop(0)
            temp1, temp2 = temp*2, temp*2+1
            result.extend([temp1, temp2])
        if min(result) >= 2**(cnt):
            break
        else:
            stack=result
            result=[]

    ans=0
    for i in range(0, len(result), 2):
        if tree[result[i]]==0 and tree[result[i+1]]==0:
            ans+=tree[result[i]//2]
        else:
            ans+=(tree[result[i]]+tree[result[i+1]])

    print(f'#{test_case} {ans}')