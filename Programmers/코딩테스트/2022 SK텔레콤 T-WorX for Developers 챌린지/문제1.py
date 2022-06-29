def solution(p):
    answer = [0] * len(p)
    for i in range(len(p)):
        min_idx, min_val = i, p[i]
        for j in range(i+1, len(p)):
            if min_val > p[j]:
                min_idx, min_val = j, p[j]
        
        if i != min_idx:
            p[i], p[min_idx] = p[min_idx], p[i]
            answer[i] += 1
            answer[min_idx] += 1
            
    return answer


if __name__ == "__main__":
    p = [2, 3, 4, 5, 6, 1]
    print(solution(p))