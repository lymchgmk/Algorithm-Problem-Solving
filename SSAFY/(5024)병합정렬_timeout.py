import time
start_time = time.time()


def merge(left, right):
    # 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
    result = []

    #  병합과정 실행
    #  각각의 최소값들(가장 앞쪽 값)을 비교해서 더 작은 요소를 결과에 추가
    # 두 부분집합에 요소가 없어질 때까지 계속 반복
    while left or right:
        # 두 부분집합의 요소가 모두 남아 있을 경우
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            # 하나씩 복사
            result.append(left.pop(0))
            # # 한번에 나머지를 뒤에 붙임
            # result.extend(left)
            # left.clear()
        elif right:
            result.append(right.pop(0))
            # result.extend(right)
            # right.clear()
    return result


def merge_sort(a):
    global cnt
    # 문제를 절반으로 나누어서 각각을 해결하는 부분
    if len(a) == 1:
        return a
    # 절반으로 나누어서 각각 별도의 정렬 실행
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:  # 왼쪽 마지막 원소가 큰 경우
            cnt += 1

        return merge(left, right)

import sys
sys.stdin = open('(5204)병합정렬_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    A = merge_sort(A)
    print('#{} {} {}'.format(tc, A[N//2], cnt))

print(time.time() - start_time, 'seconds')