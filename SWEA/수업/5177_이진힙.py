import sys, heapq
sys.stdin=open('5177_이진힙.txt')

T=int(input())

for test_case in range(1, T+1):
    N=int(input())
    data=list(map(int, input().split()))
    test=[]
    for d in data:
        test.append(d)
        heapq.heapify(test)

    mother=[]
    while N !=1:
        N=N//2
        mother.append(N)

    ans=0
    for m in mother:
       ans+=test[m-1]

    print(f'#{test_case} {ans}')