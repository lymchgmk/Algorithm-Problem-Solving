def solution(n):
    def reversed_tri(n):
        res = ''
        while n:
            q, r = divmod(n, 3)
            n = q
            res += str(r)
        return res
    
    answer = int(reversed_tri(n), 3)
    return answer


n = 125
print(solution(n))