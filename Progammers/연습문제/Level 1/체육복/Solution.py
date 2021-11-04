def solution(n, lost, reserve):
    before, after = [False] + [1] * n, [False] + [0] * n
    for l in lost:
        before[l] -= 1
    for r in reserve:
        before[r] += 1
    
    for i, cnt in enumerate(before):
        if cnt == 0:
            continue
        elif cnt == 1:
            after[i] = 1
        else: # cnt == 2:
            after[i] = 1
            if i != 1 and after[i-1] == 0:
                after[i-1] = 1
            elif i != n and after[i+1] == 0:
                after[i+1] = 1
    
    return after.count(1)


if __name__ == "__main__":
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    print(solution(n, lost, reserve))
