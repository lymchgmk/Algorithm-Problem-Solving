# 셀렉션 = 정렬 후 + 원하는 순서 뽑기
def selectionsort(list, k):
    for i in range(0, k):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

    return list[k-1]

data = [64, 25, 10, 22, 11]


# 정렬 말고 큰 거 or 작은거 k번 찾는게 더 쉽다