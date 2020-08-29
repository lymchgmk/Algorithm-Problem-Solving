import sys
sys.stdin = open("(1959)두개의숫자열_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arrN = list(map(int, input().split()))
    arrM = list(map(int, input().split()))

    if N < M:
        arrN, arrM = arrM, arrN
        N, M = M, N

    max = 0
    for i in range(len(arrN)-len(arrM)+1):
        sum = 0
        for j in range(len(arrM)):
            sum += arrN[i+j]*arrM[j]
        if max < sum:
            max = sum

    print("#{} {}".format(tc+1, max))