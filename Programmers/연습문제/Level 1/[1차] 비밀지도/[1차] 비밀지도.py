def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        _bin = str(bin(arr1[i]|arr2[i]))[2:]
        _bin = _bin.rjust(n, '0')
        answer.append(_bin.replace('1', '#').replace('0', ' '))
    return answer


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))