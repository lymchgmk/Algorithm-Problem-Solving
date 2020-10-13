def X_scale(number, X):
    q, r = divmod(number, X)
    if q == 0:
        return str(r)
    else:
        return X_scale(q, X) + str(r)


def solution(N):
    sub_result = []
    for i in range(2, 10):
        sub_result.append([X_scale(N, i), i])

    result = []
    for j in range(8):
        test = sub_result[j][0]
        temp = 1
        for n in test:
            if n != 0:
                temp *= int(n)
        result.append([temp, j+2])

    result = sorted(result, key = lambda x : (-x[0], -x[1]))
    answer = [result[0][1], result[0][0]]
    
    return answer

    