def solution(a):
    def powerset(s):
        masks = [1 << i for i in range(len(s))]
        for i in range(1 << len(s)):
            yield [ss for ss, mask in zip(s, masks) if mask & i]
    
    def is_star(x):
        if len(x) < 2 or len(x) % 2:
            return False
        
        test_inter = [[x[2*i], x[2*i + 1]] for i in range(len(x) // 2)]
        
        for t0, t1 in test_inter:
            if t0 == t1:
                return False
            
        tmp = set(test_inter[0])
        for i in range(1, len(x)//2):
            tmp &= set(test_inter[i])
            if not tmp:
                return False
        
        return True
    
    answer = 0
    _powerset = powerset(a)
    for _ps in _powerset:
        if is_star(_ps):
            answer = max(answer, len(_ps))
    return answer


a = [0,3,3,0,7,2,0,2,2,0]
print(solution(a))