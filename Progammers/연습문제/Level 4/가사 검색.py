# from collections import defaultdict
# from bisect import bisect_left, bisect_right
#
#
# def solution(words, queries):
#     def _bisect(lst, start, end):
#         return bisect_right(lst, end) - bisect_left(lst, start)
#
#     answer = []
#     cands = defaultdict(list)
#     reversed_cands = defaultdict(list)
#
#     for word in words:
#         cands[len(word)].append(word)
#         reversed_cands[len(word)].append(word[::-1])
#
#     for cand in cands.values():
#         cand.sort()
#     for rev_cand in reversed_cands.values():
#         rev_cand.sort()
#
#     for query in queries:
#         if query[0] == '?':
#             lst = reversed_cands[len(query)]
#             start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
#         else:
#             lst = cands[len(query)]
#             start, end = query.replace('?', 'a'), query.replace('?', 'z')
#
#         answer.append(_bisect(lst, start, end))
#
#     return answer


def solution(words, queries):
    class Node:
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.children = {}
    
    class Trie:
        pass
    
    
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
