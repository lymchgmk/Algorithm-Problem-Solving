import sys
from collections import defaultdict
sys.stdin = open("7432_디스크 트리.txt", "rt")


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        node = self.root
        for word in words:
            node = node.children[word]
        node.end = True

    def traversal(self, level, node):
        for child in sorted(node.children):
            print(' '*level + child)
            self.traversal(level+1, node.children[child])


def solution(N, directory):
    trie = Trie()
    for words in directory:
        trie.insert(words)

    trie.traversal(0, trie.root)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    directory = [input().split("\\") for _ in range(N)]
    solution(N, directory)
