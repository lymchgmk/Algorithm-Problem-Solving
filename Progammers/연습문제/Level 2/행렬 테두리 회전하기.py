def solution(rows, columns, queries):
    def rotate(arr, query):
        x1, y1, x2, y2 = map(lambda x: x-1, query)
        print(x1, y1, x2, y2)
        
        return arr, 0
    
    
    arr = [[c*rows + r + 1 for r in range(rows)] for c in range(columns)]
    answer = []
    for query in queries:
        arr, min_value = rotate(arr, query)
        answer.append(min_value)
    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))