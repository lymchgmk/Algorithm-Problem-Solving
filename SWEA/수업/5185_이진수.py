import sys
sys.stdin=open('5185_이진수.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = input().split()
    N=int(N)
    M=list(M)

    result=[]
    for char in M:
        temp='0x' + char
        temp=bin(int(temp, 16))[2:]
        if len(temp) < 4:
            temp = '0'*(4-len(temp)) + str(temp)
        result.append(temp)

    ans=str()
    for r in result:
        ans += r

    print(f'#{test_case} {ans}')