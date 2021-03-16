import collections


def solution(n, vertex):
    def bfs(start):
        deq = collections.deque([start])
        visited[start] = 1
        while deq:
            temp = deq.popleft()
            for next in adj[temp]:
                if not visited[next]:
                    visited[next] = True
                    deq.append(next)
                    visited[next] = visited[temp]+1
                    max_dist = visited[next]
        return visited.count(max_dist)
            
    adj = collections.defaultdict(list)
    for s, e in vertex:
        adj[s].append(e)
        adj[e].append(s)
    
    visited = [0]*(n+1)
    
    answer = bfs(1)
    return answer



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# print(solution(n, vertex))
#
#
# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
# print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
# print(solution(2, [[1, 2]]), 1)
# print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
# print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
# print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
# print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
# print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)