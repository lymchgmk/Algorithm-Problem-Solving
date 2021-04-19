# import re
#
#
# def solution(words, queries):
#     answer = [0]*len(queries)
#     for idx, query in enumerate(queries):
#         pattern = query.replace('?', '.')
#         for word in words:
#             if re.fullmatch(pattern, word):
#                 answer[idx] += 1
#     return answer
#
#
# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# print(solution(words, queries))


from collections import defaultdict
from bisect import bisect_left, bisect_right


def count():
    pass

def solution(words, queries):
    answer = []
    cands = defaultdict(list)
    reversed_cands = defaultdict(list)
    
    for word in words:
        cands[len(word)].append(word)
        reversed_cands[len(word)].append(word[::-1])
        
    print('cand', cands)
    print('rev_cand', reversed_cands)
    
    for cand in cands.values():
        cand.sort()
    for rev_cand in reversed_cands.values():
        rev_cand.sort()
    
    print('cand', cands)
    print('rev_cand', reversed_cands)
    
    for query in queries:
        if query[0] == '?':
            pass
        else:
            pass
    
    
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
