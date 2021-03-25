# 16진수까지 쓰이는 숫자들
num_notations = '0123456789ABCDEF'


def n_base(num, base):
    q, r = divmod(num, base)
    n = num_notations[r]
    return n_base(q, base) + n if q else n
