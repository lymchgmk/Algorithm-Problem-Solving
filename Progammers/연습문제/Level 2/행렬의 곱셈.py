def solution(arr1, arr2):
    x1, y1 = len(arr1), len(arr1[0])
    x2, y2 = len(arr2), len(arr2[0])
    answer = [[0] * y2 for _ in range(x1)]
    
    for i in range(x1):
        row1 = arr1[i]
        for j in range(y2):
            col2 = [a2[j] for a2 in arr2]
            for r, c in zip(row1, col2):
                answer[i][j] += r*c
    
    return answer


arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = 	[[3, 3], [3, 3]]
print(solution(arr1, arr2))
    