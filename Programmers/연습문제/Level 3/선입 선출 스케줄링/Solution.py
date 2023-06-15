def solution(n, cores):
    if n < len(cores):
        return n

    n -= len(cores)

    left, right = 1, max(cores) * n
    while left < right:
        mid = left + (right - left) // 2
        works = sum([mid // core for core in cores])

        if works < n:
            left = mid + 1
        else:
            right = mid

    work_hours = left
    works_per_core_without_last_work_hour = [(work_hours - 1) // core for core in cores]
    remain_works_for_last_hour = n - sum(works_per_core_without_last_work_hour)

    for idx, core in enumerate(cores, start=1):
        core_can_work_at_last_hour = (work_hours % core == 0)
        if core_can_work_at_last_hour:
            remain_works_for_last_hour -= 1

            if remain_works_for_last_hour == 0:
                return idx


if __name__ == "__main__":
    n = 6
    cores = [1, 2, 3]
    result = 2
    answer = solution(n, cores)
    print(result == answer, answer)
