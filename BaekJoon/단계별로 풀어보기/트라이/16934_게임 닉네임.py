import sys
from collections import defaultdict
sys.stdin = open("16934_게임 닉네임.txt", "rt")


class TrieNode:
    def __init__(self):
        self.end = 0
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def nickname(self, word):
        node = self.root
        res = ""
        stop = False
        for char in word:
            if char in node.children:
                res += char
            else:
                if not stop:
                    res += char
                    stop = True
            node = node.children[char]

        node.end += 1
        if node.end > 1:
            res += str(node.end)
        print(res)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    trie = Trie()
    for _ in range(N):
        trie.nickname(input())
