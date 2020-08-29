# #1. for문 중첩해서 구하는 경우
# arr = [1, 2, 3, 4]
# bit = [0]*4
# for i in range(2):
#     bit[0] = i*arr[0]
#     for j in range(2):
#         bit[1] = j*arr[1]
#         for k in range(2):
#             bit[2] = k*arr[2]
#             for l in range(2):
#                 bit[3] = l*arr[3]
#                 print(bit)


# #2. 비트연산자 사용(내가 검색해서 찾은 경우)
# def powerset(s):
#     for i in range(1 << len(s)):
#         print([s[j] for j in range(len(s)) if (i & (1 << j))])
#
# powerset([1, 2, 3, 4])
# powerset((1, 2, 3, 4))
# powerset('1234')


# #3. 알고리즘 강사님 (bit order)
# arr = [3, 6, 7, 1, 5 ,4]
#
# n = len(arr) # n: 원소의 갯수
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print([arr[j], end=", "])


#  # 3-1. 부분집합의 합이 10인 부분집합을 추출
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def powerset_sum(list):
#     for i in range(1 << len(list)):
#         if sum([list[j] for j in range(len(list)) if i & (1 << j)]) == 10:
#             print([list[j] for j in range(len(list)) if i & (1 << j)])
#
# powerset_sum(arr)


# 3-2. 강사님 부분집합 풀이
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j): sum += arr[j]

    if sum == 10:
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end=" ")
        print()