def solution(words):
    class Node:
        def __init__(self, key, cnt=0):
            self.key = key
            self.cnt = cnt
            self.children = {}

    trie = {}
    for word in words:
        cur_trie = trie
        for char in word:
            if not cur_trie.get(char):
                cur_trie[char] = Node(key=char)
            cur_trie[char].cnt += 1
            cur_trie = cur_trie[char].children
           
    result = 0
    for word in words:
        cur_trie = trie
        for idx, char in enumerate(word):
            if cur_trie[char].cnt == 1:
                break
            else:
                cur_trie = cur_trie[char].children
        # break하거나 break하지 않고 for문이 끝나거나 둘 다 잡아주려면 if-else말고 이렇게
        result += idx + 1
    return result
    
    
words = ["go","gone","guild"]
print(solution(words))
