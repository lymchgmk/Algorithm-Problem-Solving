import sys
sys.stdin=open("5207_이진 탐색.txt")

def my_binary_search(data, test):
    global count
    status=0 # 좌 = -1 / 우 = +1
    start, end = 0, len(data)-1

    while start <= end:
        mid = (start + end) // 2

        if test == A[mid]: # 1/3 mid 와 같은 경우
            count += 1
            break

        elif test > A[mid]: # 2/3 우측에 속한 경우
            start = mid + 1
            if status == 1: # 2번 우측에 속한 경우 (==번갈아X)
                break
            else:
                status = 1

        elif test < A[mid]: # 3/3 좌측에 속한 경우
            end = mid - 1
            if status == -1: # 2번 좌측에 속한 경우 (==번갈아X)
                break
            else:
                status = -1

T=int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split()))) # 정렬해줘야함
    B = list(map(int, input().split()))

    count = 0
    for b in B:
        my_binary_search(A, b)

    print(f'#{test_case} {count}')