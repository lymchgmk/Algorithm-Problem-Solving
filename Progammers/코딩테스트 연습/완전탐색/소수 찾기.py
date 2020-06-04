from itertools import permutations
numbers = "01"

def is_this_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True


def my_solution(numbers):
    numbers = list(numbers)

    result = []
    for i in range(1, len(numbers)+1):
        for subset in permutations(numbers, i):
            temp = int(''.join(subset))
            if temp not in result:
                result.append(temp)

    cnt = 0
    for number in result:
        if is_this_prime(number):
            cnt += 1

    return cnt


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


print(my_solution(numbers))

print(solution(numbers))