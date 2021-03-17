def solution(math_scores, english_scores):
    def make_rank_list(subject):
        L = len(subject)
        subject_rank = []
        for i in range(L):
            temp_rank = 1
            for j in range(L):
                if i != j and subject[i] < subject[j]:
                    temp_rank += 1
            subject_rank.append(temp_rank)
        return subject_rank
    
    math_rank = make_rank_list(math_scores)
    english_rank = make_rank_list(english_scores)
    
    answer = 0
    for i in range(len(math_rank)):
        for j in range(i + 1, len(math_rank)):
            if (math_rank[i] > math_rank[j] and english_rank[i] > english_rank[j]) or (
                    math_rank[i] < math_rank[j] and english_rank[i] < english_rank[j]):
                answer += 1
    return answer


math_scores = [70, 65, 90, 80, 50]
english_scores = [40, 20, 30, 60, 50]
print(solution(math_scores, english_scores))