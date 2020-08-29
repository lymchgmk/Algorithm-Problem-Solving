numbers = [1, 1, 1, 1, 1]
target = 3

check = []
vector = []
answer = 0


def cal(target, numbers):
    global vector, answer
    temp = [i for i in numbers]

    for i in vector:
        temp[i] *= -1

    sum = 0
    for i in temp:
        sum += i

    if target == sum:
        answer += 1


def solve(cnt, standard, end, numbers, target):
    global check, vector

    if cnt == end:
        cal(target, numbers)
        return

    for i in range(standard, len(numbers)):
        if check[i] == False:
            check[i] = True
            vector.append(i)
            solve(cnt + 1, i, end, numbers, target)
            vector.pop()
            check[i] = False


def solution(numbers, target):
    global check, answer

    for k in range(1, len(numbers), 1):
        vector = []
        check = [False for i in range(0, 20, 1)]
        solve(0, 0, k, numbers, target)

    return answer

print(solution(numbers, target))