import collections


def solution(n, results):
    answer = 0
    wins = collections.defaultdict(set)
    loses = collections.defaultdict(set)
    
    for w, l in results:
        wins[w].add(l)
        loses[l].add(w)
    
    for i in range(1, n + 1):
        for loser in wins[i]:
            loses[loser] |= loses[i]
        for winner in loses[i]:
            wins[winner] |= wins[i]
            
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
    
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
