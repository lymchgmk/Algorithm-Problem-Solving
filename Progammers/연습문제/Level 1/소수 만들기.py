import itertools


def solution(nums):
    def isPrime(num):
        for i in range(2, int(num**0.5)+1):
            if not num % i:
                return False
        else:
            return True
    
    answer = 0
    comb = itertools.combinations(nums, 3)
    for c in comb:
        if isPrime(sum(c)):
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]
print(solution(nums))