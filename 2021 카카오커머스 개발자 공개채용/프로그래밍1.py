from itertools import product


def solution(n, p, c):
    def pow_mod(num, p, mod):
        res = 1
        while p:
            if p & 1:
                res = (res * num) % mod
            num = (num ** 2) % mod
            p >>= 1
        return res
    
    answer = [0]*n
    num_remain = {num: pow_mod(num, p, n) for num in range(n)}
    a_list = [list(range(n)) for _ in range(c)]
    for pd in product(*a_list):
        remain_sum = 0
        for num in pd:
            remain_sum += num_remain[num]
            remain_sum %= n
        answer[remain_sum] += 1
    
    return [ans % 101 for ans in answer]

n, p, c = 2, 3, 4
print(solution(n, p, c))