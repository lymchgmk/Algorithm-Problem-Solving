from itertools import combinations


def is_prime(target):
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combs = combinations(nums, 3)
    for comb in combs:
        if is_prime(sum(comb)):
            answer += 1
    return answer