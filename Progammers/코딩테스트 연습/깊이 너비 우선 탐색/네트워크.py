def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack = [i]
            while stack:
                temp = stack.pop()
                for i in range(n):
                    if not visited[i] and computers[temp][i]:
                        stack.append(i)
                        visited[i] = True
            answer += 1
            
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 0, 1]]
print(solution(n, computers))