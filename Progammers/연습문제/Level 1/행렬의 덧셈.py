def solution(arr1, arr2):
    return [[n1+n2 for n1, n2 in zip(row1, row2)]for row1, row2 in zip(arr1, arr2)]