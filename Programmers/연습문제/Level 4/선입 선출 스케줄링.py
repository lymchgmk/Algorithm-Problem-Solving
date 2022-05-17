def solution(n, cores):
    if n <= len(cores):
        return n

    n -= len(cores)
    left, right = 1, max(cores) * n
    while left < right:
        mid = (left + right) // 2
        
        workload = sum([mid//core for core in cores])
        if workload >= n:
            right = mid
        else:
            left = mid + 1
    
    work_time = right
    work_per_core = [(work_time - 1) // core for core in cores]
    n -= sum(work_per_core)
    
    for idx, core in enumerate(cores, start=1):
        if work_time % core == 0:
            n -= 1
            if n == 0:
                return idx


n = 6
cores = [1, 2, 3]
print(solution(n, cores))
