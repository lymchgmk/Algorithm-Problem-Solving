def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    mst = {costs[0][0]}
    while len(mst) != n:
        for idx, [s, e, dist] in enumerate(costs):
            if s in mst and e in mst:
                continue
            elif s in mst or e in mst:
                mst.update([s, e])
                answer += dist
                costs[idx] = [-1, -1, -1]
                break
    return answer


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))