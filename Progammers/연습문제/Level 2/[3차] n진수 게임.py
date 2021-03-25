def solution(n, t, m, p):
    num_notations = '0123456789ABCDEF'
    def n_base(num, base):
        q, r = divmod(num, base)
        n = num_notations[r]
        return n_base(q, base) + n if q else n
    
    answer = ''
    num = 0
    while len(answer) < t*m:
        answer += n_base(num, n)
        num += 1
    
    return answer[p-1::m][:t]


n = 2
t = 4
m = 2
p = 1
print(solution(n, t, m, p))