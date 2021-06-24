def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:        #검색성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    return False # 검색실패

# key = 7
key = 22
data = [2,4,7,9,11,19,23]
print(binarySearch(data, key))