from collections import Counter


def solution(scores):
    def make_grade(points):
        if points >= 90:
            return 'A'
        elif 90 > points >= 80:
            return 'B'
        elif 80 > points >= 70:
            return 'C'
        elif 70 > points >= 50:
            return 'D'
        else:
            return 'F'
    
    scores_dict = {i: [] for i in range(len(scores))}
    for score in scores:
        for idx, point in enumerate(score):
            scores_dict[idx].append(point)
    
    answer = ''
    for student, score in scores_dict.items():
        student_score = score[student]
        counter = Counter(score)
        _sum, L = sum(score), len(score)
        _max, _min = max(score), min(score)
        if counter[student_score] == 1 and student_score in (_min, _max):
            _sum -= score[student]
            L -= 1
        
        answer += make_grade(_sum/L)
    return answer
            
    
if __name__ == '__main__':
    #
    scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
    # scores = [[70,49,90],[68,50,38],[73,31,100]]
    #
    print(solution(scores))
    