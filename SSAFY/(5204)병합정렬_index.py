import time
start_time = time.time()
def merge_sort(a):
    global cnt
    if len(a) == 1:                     # 리스트 원소가 하나 남을 때
        return a
    else:
        m = len(a)//2
        left = a[:m]                    # 리스트 왼쪽 절반
        right = a[m:]                   # 오른쪽 절반
        left = merge_sort(left)         # 정렬된 리스트 리턴
        right = merge_sort(right)       # 정렬된 리스트 리턴

        left_idx = 0
        right_idx = 0
        i = 0
        while left_idx < len(left) and right_idx < len(right):  # 좌우 리스트에서 비교 대상이 남은 경우
            if left[left_idx] < right[right_idx]:
                a[i] = left[left_idx]
                left_idx += 1
            else:
                a[i] = right[right_idx]
                right_idx += 1
            i += 1

        if left_idx < len(left):        # 왼쪽 리스트가 남은 경우
            a[i:] = left[left_idx:]
    
        if right_idx < len(right):      # 오른쪽 리스트가 남은 경우
            a[i:] = right[right_idx:]

        if left[-1] > right[-1]:        # 왼쪽 마지막 원소가 큰 경우(문제)
            cnt += 1
        return a                        # 왼쪽 오른쪽을 합쳐 정렬된 리스트 반환

import sys
sys.stdin = open('(5204)병합정렬_input.txt', 'r')
T = int(input())

for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    A = merge_sort(A)
    print('#{} {} {}'.format(tc+1, A[N//2], cnt))

print(time.time() - start_time, 'seconds')

