def solution(n):
    q, r = divmod(n, 2)
    return '수박'*q + '수박'[:r]