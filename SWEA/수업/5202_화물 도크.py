import sys
sys.stdin=open("5202_화물 도크.txt")

def docking_plan(start):
    end=start[1]
    cnt=1
    for i in range(1, N):
        if end <= lorrys[i][0]:
            end=lorrys[i][1]
            cnt+=1
    return cnt

T=int(input())

for test_case in range(1, T+1):
    N=int(input())
    se=[list(map(int, input().split())) for _ in range(N)]

    lorrys=sorted(se, key=lambda x: x[1])

    answer=0
    for lorry in lorrys:
        result=docking_plan(lorry)
        if result > answer:
            answer=result

    print(f'#{test_case} {answer}')