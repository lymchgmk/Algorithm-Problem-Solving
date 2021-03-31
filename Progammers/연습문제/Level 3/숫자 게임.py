def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    for a in A:
        while B:
            b = B.pop(0)
            if a < b:
                answer += 1
                break
    return answer


A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
print(solution(A, B))
