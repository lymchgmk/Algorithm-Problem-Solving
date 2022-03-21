import sys
from collections import defaultdict
sys.stdin = open("9250_문자열 집합 판별.txt", "r")


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.end = True

    def query(self, word):
        for idx in range(len(word)):
            char = word[idx]
            node = self.root
            if char in node.children:
                sub_word = char
                node = node.children[char]
                idx += 1
                while idx < len(word) and word[idx] in node.children:
                    sub_word += word[idx]
                    node = node.children[word[idx]]
                    idx += 1
                if len(sub_word) >= 2:
                    print(sub_word)
                    return "YES"
        return "NO"


if __name__ == "__main__":
    trie = Trie()
    N = int(input())
    for _ in range(N):
        trie.insert(input())
    Q = int(input())
    for _ in range(Q):
        print(trie.query(input()))
