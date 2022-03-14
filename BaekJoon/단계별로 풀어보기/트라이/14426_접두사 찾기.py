import sys
from collections import defaultdict
sys.stdin = open("14426_접두사 찾기.txt", "rt")


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

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if node.end or char not in node.children:
                return False
            node = node.children[char]
        return True


def solution(N, M, S, prefix):
    trie = Trie()
    for word in S:
        trie.insert(word)

    cnt = 0
    for pf in prefix:
        if trie.starts_with(pf):
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    prefix = [input() for _ in range(M)]
    solution(N, M, S, prefix)
