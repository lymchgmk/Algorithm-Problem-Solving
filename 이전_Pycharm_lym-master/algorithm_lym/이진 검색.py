# 이진검색은 정렬된 경우만 가능

#1. 구현
def binarysearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return -1

a = [2, 4, 7, 9, 11, 19, 23]
key = 19
print(binarysearch(a, key))
print(a[binarysearch(a, key)])

#2. 재귀
def binarysearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low+high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarysearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarysearch2(a, middle+1, high, key)