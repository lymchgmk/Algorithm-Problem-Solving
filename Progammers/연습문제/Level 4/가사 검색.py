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
        def __init__(self, key):
            self.key = key
            self.remain_length = {}
            self.children = {}
    
    class Trie:
        def __init__(self):
            self.head = Node(None)
        
        def insert(self, string):
            curr_node = self.head
            
            remain_length = len(string)
            if remain_length in curr_node.remain_length:
                curr_node.remain_length[remain_length] += 1
            else:
                curr_node.remain_length[remain_length] = 1
            
            for char in string:
                if char not in curr_node.children:
                    curr_node.children[char] = Node(char)
                    
                curr_node = curr_node.children[char]
                remain_length -= 1
                if remain_length in curr_node.remain_length:
                    curr_node.remain_length[remain_length] += 1
                else:
                    curr_node.remain_length[remain_length] = 1
        
        def search_count(self, string, check_length):
            curr_node = self.head
            
            if check_length + len(string) not in curr_node.remain_length:
                return 0
            
            for char in string:
                if char in curr_node.children:
                    curr_node = curr_node.children[char]
                else:
                    return 0
                
            if check_length in curr_node.remain_length:
                return curr_node.remain_length[check_length]
            else:
                return 0
            
    t = Trie()
    inv_t = Trie()
    for word in words:
        t.insert(word)
        inv_t.insert(word[::-1])
        
    answer = []
    for query in queries:
        if query.startswith('?'):
            inv_query = query[::-1]
            chars = inv_query.replace('?', '')
            check_length = len(inv_query) - len(chars)
            answer.append(inv_t.search_count(chars, check_length))
        else:
            chars = query.replace('?', '')
            check_length = len(query) - len(chars)
            answer.append(t.search_count(chars, check_length))
    
    return answer

    
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
