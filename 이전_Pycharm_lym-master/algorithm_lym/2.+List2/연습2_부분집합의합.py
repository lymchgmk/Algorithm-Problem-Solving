'''
10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
'''

# arr = list(map(int, input().split()))
arr = [1,2,3,4,5,6,7,8,9,10]

for i in range(1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j):
            sum += arr[j]

    if sum == 10:
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end= " ")
        print()