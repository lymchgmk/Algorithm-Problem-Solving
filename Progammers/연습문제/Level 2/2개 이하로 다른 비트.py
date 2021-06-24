def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            target = number+(number^(number+1)+1)//4 + 1
            answer.append(target)
    return answer

'''
def solution(numbers):
    return [((num ^ (num+1)) >> 2) + num + 1 for num in numbers]
'''


def sol2(numbers):
    for n in numbers:
        print(n, bin(n), bin(n ^ ((n + 1) >> 2)))


numbers = [2, 7]
# print(solution(numbers))
print(sol2(numbers))
