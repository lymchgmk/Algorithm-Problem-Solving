def solution(n, m):
    import math
    
    GCD = math.gcd(n, m)
    return [GCD, n*m//GCD]