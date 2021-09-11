import re


def make_base_number(num, base):
    num_notations = '0123456789'
    q, r = divmod(num, base)
    n = num_notations[r]
    return make_base_number(q, base) + n if q else n


def is_prime(number):
    number = int(number)
    if number < 2:
        return False

    for d in range(2, int(number**0.5 + 1)):
        if number % d == 0:
            return False
    else:
        return True

def solution(n, k):
    k_base = make_base_number(n, k)
    print(k_base)

    p1 = re.compile(f'0[1-9]+0')
    p2 = re.compile(f'[^0]*[1-9]+0')
    p2_sub = re.compile(f'^[1-9]+0')
    p3 = re.compile(f'0[1-9]+[^0]*')
    p3_sub = re.compile(f'0[1-9]+$')
    p4 = re.compile(f'[1-9]+')

    fa1 = re.findall(p1, k_base)
    fa2 = re.findall(p2, k_base)
    fa2_sub = re.findall(p2_sub, k_base)
    fa3 = re.findall(p3, k_base)
    fa3_sub = re.findall(p3_sub, k_base)
    fa4 = re.fullmatch(p4, k_base)

    print(fa1)
    print(fa2)
    print(fa2_sub)
    print(fa3)
    print(fa3_sub)
    print(fa4)
    print()
    # res = fa1 + fa2 + fa3
    #
    # answer = []
    # for num in res:
    #     if is_prime(num):
    #         answer.append(num)
    # if fa4:
    #     answer.append(int(k_base))
    # return len(answer)


n = 437674
k = 3
print(solution(n, k)) # 3

n = 110011
k = 10
print(solution(n, k)) # 2

n = 17
k = 10
print(solution(n, k)) # 1

n = 300
k = 10
print(solution(n, k))
