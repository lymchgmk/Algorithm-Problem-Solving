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
print(prime_nums)

left, right = 0, 0
while left