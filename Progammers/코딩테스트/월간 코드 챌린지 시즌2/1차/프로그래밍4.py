def solution(n, z, roads, queries):
    dp = [0]*max(queries)
    

n = 5
z = 5
roads = [[1,2,3],[0,3,2]]
queries = [0,1,2,3,4,5,6]
print(solution(n, z, roads, queries))
