# 풀이 1. 딕셔너리를 이용해 간결한 트라이 구현
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
        
    
    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.word
    
    
    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
