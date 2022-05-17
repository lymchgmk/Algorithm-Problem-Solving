def solution(N, stages):
    fail = {i: [0, 0] for i in range(1, N + 2)}
    for player in stages:
        fail[player][0] += 1
        if player == N+1:
            fail[player][1] += 1
    for player in range(N, 0, -1):
        fail[player][1] += fail[player+1][1] + fail[player][0]
    del fail[N+1]
    
    result = []
    for key in fail:
        p = fail[key][0] / fail[key][1] if fail[key][1] else 0
        result.append([key, p])
    
    result.sort(key=lambda x: [-x[1], x[0]])

    return [r[0] for r in result]


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))