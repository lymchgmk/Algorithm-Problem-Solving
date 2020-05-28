from queue import PriorityQueue

def solution(priorities, location):
    answer = 0

    PQ = PriorityQueue()
    solve = []

    for doc, pri in enumerate(priorities):
        PQ.put((-pri, doc+1))

    for i in range(len(priorities)):
        solve.append(PQ.get()[1])
    print(solve)

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))