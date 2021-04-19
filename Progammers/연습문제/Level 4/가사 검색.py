import re


def solution(words, queries):
    answer = [0]*len(queries)
    for idx, query in enumerate(queries):
        pattern = query.replace('?', '.')
        for word in words:
            if re.fullmatch(pattern, word):
                answer[idx] += 1
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
