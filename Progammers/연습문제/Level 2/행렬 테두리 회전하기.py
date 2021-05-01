def solution(rows, columns, queries):
    def rotate(arr, query):
        x1, y1, x2, y2 = map(lambda x: x - 1, query)
        min_cand, tmp = [], 0
        for y in range(y1, y2):
            arr[x1][y], tmp = tmp, arr[x1][y]
            min_cand.append(tmp)
        for x in range(x1, x2):
            arr[x][y2], tmp = tmp, arr[x][y2]
            min_cand.append(tmp)
        for y in range(y2, y1, -1):
            arr[x2][y], tmp = tmp, arr[x2][y]
            min_cand.append(tmp)
        for x in range(x2, x1-1, -1):
            arr[x][y1], tmp = tmp, arr[x][y1]
            min_cand.append(tmp)
        return arr, min(min_cand[:-1])
        
    arr = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    answer = []
    for query in queries:
        arr, min_value = rotate(arr, query)
        answer.append(min_value)
    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))