baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]


from itertools import permutations


def baseball_game(n1, n2):
    strike, ball = 0, 0
    n2_list = list(map(int, str(n2[0])))

    for i in range(3):
        for j in range(3):
            if n1[i] == n2_list[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    if [strike, ball] == [n2[1], n2[2]]:
        return True
    else:
        return False


def my_solution(baseball):
    answer = 0

    sample = permutations(list(range(1, 10)), 3)
    for s in sample:
        flag = 0
        for b in baseball:
            if not baseball_game(s, b):
                break
            else:
                flag += 1
        if flag == len(baseball):
            answer += 1

    return answer

print(my_solution(baseball))