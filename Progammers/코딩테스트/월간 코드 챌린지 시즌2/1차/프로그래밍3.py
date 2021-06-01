from collections import deque


def solution(a, edges):
    if sum(a):
        return -1
    
    cntr = [0]*len(a)
    for p1, p2 in edges:
        cntr[p1] += 1
        cntr[p2] += 1

    answer = 0
    deq_edges = deque(edges)
    while deq_edges:
        p1, p2 = deq_edges.popleft()
        if cntr[p1] == 1:
            answer += abs(a[p1])
            cntr[p1] -= 1
            cntr[p2] -= 1
            a[p2] += a[p1]
            a[p1] = 0
        else:
            deq_edges.append([p2, p1])

    if not any(a):
        return answer
    else:
        return -1


a = [-3, 2, 0, 0, 1]
edges = [[0, 1], [3, 4], [2, 3], [1, 3]]
print(solution(a, edges))
