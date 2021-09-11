from collections import Counter


def solution(a):
    if len(a) <= 1:
        return 0

    cnt_n = Counter(a).most_common()
    cnt_n = {n: cnt for n, cnt in cnt_n}
    print(cnt_n)

    answer = 0
    for n in cnt_n:
        if cnt_n[n] * 2 <= answer:
            continue
        
        index = 1
        cnt = 0
        while index < len(a):
            if (a[index - 1] != n and a[index] != n) or a[index - 1] == a[index]:
                index += 1
                continue
            
            cnt += 2
            index += 2
        
        answer = max(answer, cnt)
    
    return answer


print(solution([1, 2, 3, 1, 4, 5, 6, 1]))


a = [0,3,3,0,7,2,0,2,2,0]
print(solution(a))