def quick_sort(arr, left, right): # 왼쪽 시작점, 오른쪽 끝 지점
    # pivot 위치 결정 (pivot을 기준으로 큰 값은 오른쪽, 작은 값은 왼쪾으로 구분)
    # 왼쪽 부분집합 정렬
    # 오른쪽 부분집합 정렬
    if left > right:
    # pivot 구하기
        pivot = hoare_partition(arr, left, right)
        # 왼쪽 부분집합 정렬 실행
        quick_sort(arr, left, pivot-1)
        # 오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot+1, right)


def hoare_partition(arr, left, right):
    # i, j를 설정하고, 큰 값 찾고, 작은 값 찾아서 위치 바꿔주기
    i=left
    j=right
    pivot=arr[left]
    # i가 j보다 작을 때 까지 계속해서 반복
    while i <= j:
        # pivot 보다 큰 값이 나올 때 까지 i 증가
        while i <= j and arr[i] <= pivot:
            i+=1
        # pivot 보다 작은 값이 나올 때 까지 j 감소
        while i <= j and arr[j] >= pivot:
            j-=1

        # i가 j 보다 작으면 , 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]

    return j

arr = [4, 5, 1, 2, 9, 8, 3, 6, 7]
quick_sort(arr, 0, len(arr)-1)
print(arr)