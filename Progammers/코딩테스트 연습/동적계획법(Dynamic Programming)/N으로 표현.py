def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        num_set = {int(str(N) * i)}

        for j in range(i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    num_set.add(x + y)
                    num_set.add(x - y)
                    num_set.add(y - x)
                    num_set.add(x * y)

                    if y != 0:
                        num_set.add(x // y)

        if number in num_set:
            return i

        DP.append(num_set)

    return answer


N = 5
number = 12
print(solution(N, number))