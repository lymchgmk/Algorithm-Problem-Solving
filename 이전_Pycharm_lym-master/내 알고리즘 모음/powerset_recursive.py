N = 10
A = [0 for _ in range(N)]
data = list(range(1, 11))

def printset(n):
    result = []
    for i in range(n):
        if A[i] == 1:
            result.append(data[i])

    if sum(result) == 10:
        print(result)

def powerset(n, k): # n: 원소의 갯수, k: 현재 depth
    if n == k: # Basis part
        printset(n)
    else: # Inductive part
        A[k] = 1 # k번 요소 포함
        powerset(n, k+1) # 다음 요소 포함 여부 결정
        A[k] = 0 # k번 요소 미포함
        powerset(n, k+1) # 다음 요소 포함 여부 결정


powerset(N, 0)
