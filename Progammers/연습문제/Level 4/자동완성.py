# def solution(words):
#     trie = {}
#     for word in words:
#         cur_trie = trie
#         for w in word:
#             cur_trie.setdefault(w, [0, {}])
#             cur_trie[w][0] += 1
#             cur_trie = cur_trie[w][1]
#
#     result = 0
#     for word in words:
#         cur_trie = trie
#         for i in range(len(word)):
#             if cur_trie[word[i]][0] == 1:
#                 break
#             else:
#                 cur_trie = cur_trie[word[i]][1]
#         result += i+1
#     return result
from collections import defaultdict


def solution(words):
    class Node:
        def __init__(self, key, cnt=0):
            self.key = key
            self.cnt = cnt
            self.children = {}
    
    trie = defaultdict(int)
    for word in words:
        for char in word:
            if trie[char] == 0:
            
    

words = ["go","gone","guild"]
print(solution(words))
