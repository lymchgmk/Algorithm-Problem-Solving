n=7
lost=[2, 3, 4]
reserve=[1, 2, 3, 6]

def my_solution(n, lost, reserve):
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    answer = n - len(list(real_lost))
    count = 0

    for r in real_reserve:
        if r - 1 in real_lost:
            count += 1
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            count += 1
            real_lost.remove(r + 1)

    return answer + count
