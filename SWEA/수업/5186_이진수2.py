import sys
sys.stdin=open("5186_이진수2.txt")

T = int(input())

for test_case in range(1, T+1):
    N=float(input())

    if not (N*(2**12)).is_integer():
        print(f'#{test_case} overflow')
        continue

    else:
        count=1
        while not (N*(2**count)).is_integer():
            count+=1

        result=str((bin(int(N*(2**count))))[2:])
        result='0'*(count-len(result)) + result

        print(f'#{test_case} {result}')