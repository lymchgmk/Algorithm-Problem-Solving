import sys
sys.stdin = open("6588_골드바흐의 추측.txt", "rt")


def solution(n):
    def isPrime(num):
        global prime_check
        if prime_check[num]:
            return prime_check[num]

        for d in range(2, int(num**0.5) + 1):
            if num % d == 0:
                return False
        else:
            prime_check[num] = True
            return True

    for a in range(3, n+1, 2):
        b = n - a
        if isPrime(a) and isPrime(b):
            return f"{n} = {a} + {b}"
    else:
        return "Goldbach's conjecture is wrong."


if __name__ == "__main__":
    input = sys.stdin.readline
    prime_check = [False] * 1000001
    while True:
        n = int(input())
        if n == 0:
            break
        print(solution(n))
