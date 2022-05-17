def solution(n, k):
    def jinsoo(n, k):
        res = ''
        while n:
            n, r = divmod(n, k)
            res = str(r) + res
        return res

    def isPrime(num):
        num = int(num)
        if num == 1:
            return False

        for d in range(2, int(num**0.5) + 1):
            if num % d == 0:
                return False
        else:
            return True

    answer = 0
    for s in jinsoo(n, k).split('0'):
        if s and isPrime(s):
            answer += 1
    return answer


if __name__ == "__main__":
    n = 110011
    k = 10
    solution(n, k) # 1