import sys
sys.stdin = open('1644_소수의 연속합.txt', 'rt')


def is_prime_number(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


N = int(input())
prime_nums = [n for n in range(2, N+1) if is_prime_number(n)]

end = 0
partial_sum = 0
cnt = 0

for start in range(len(prime_nums)):
    while partial_sum < N and end < len(prime_nums):
        partial_sum += prime_nums[end]
        end += 1
    
    if partial_sum == N:
        cnt += 1
    partial_sum -= prime_nums[start]

print(cnt)
