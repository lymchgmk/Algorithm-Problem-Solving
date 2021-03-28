def solution(arr):
    from itertools import chain
    def quad(arr):
        L = len(arr)
        _sum = sum(chain(*arr))
        if L == 1:
            return [arr[0][0]]
        if _sum == L**2:
            return [1]
        elif _sum == 0:
            return [0]
        
        arr1, arr2, arr3, arr4 = [
            [a[:L//2] for a in arr[:L//2]],
            [a[L//2:] for a in arr[:L//2]],
            [a[:L//2] for a in arr[L//2:]],
            [a[L//2:] for a in arr[L//2:]]
        ]
        
        result = quad(arr1) + quad(arr2) + quad(arr3) + quad(arr4)
        return list(chain(result))
        
    answer = quad(arr)
    return [answer.count(0), answer.count(1)]


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))