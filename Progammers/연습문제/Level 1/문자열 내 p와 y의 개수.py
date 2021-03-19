def solution(s):
    from collections import Counter
    
    s= s.lower()
    s_counter = Counter(s)
    print(s_counter)
    if s_counter['p'] != s_counter['y']:
        return False
    return True


s = "pPoooyY"
print(solution(s))
reversed()