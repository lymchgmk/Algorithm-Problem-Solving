def solution(d, budget):
    d.sort()
    
    while sum(d) != budget:
        if sum(d) - budget in d:
            return len(d)-1
        d.pop(0)
    
    return len(d)


d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))