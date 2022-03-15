import sys
from collections import defaultdict
sys.stdin = open("9202_Boggle.txt", "rt")


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        for word in words:
            node = self.root
            for char in word:
                node = node.children[char]
            node.word = True


def dfs(trie, r, c):
    DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    res = []
    stack = [(r, c)]
    node = trie.root
    visited = [[False] * SIZE for _ in range(SIZE)]
    while stack:
        curr_r, curr_c = stack.pop()
        curr_char = boggle[curr_r][curr_c]
        if curr_char not in node.children:
            continue
        node = node.children[curr_char]
        for d_r, d_c in DIRS:
            post_r, post_c = curr_r + d_r, curr_c + d_c
            if 0 <= post_r < SIZE and 0 <= post_c < SIZE:
                post_char = boggle[post_r][post_c]
                if post_char in node.children and not visited[post_r][post_c]:



def solution(trie, boggle):
    for r in range(SIZE):
        for c in range(SIZE):
            dfs(trie, r, c)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    w = int(input())
    words = [input() for _ in range(w)]
    trie = Trie()
    trie.insert(words)
    _ = input()

    SCORES = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
    SIZE = 4
    b = int(input())
    for _ in range(b):
        boggle = [list(input()) for _ in range(4)]
        solution(trie, boggle)
        try:
            _ = input()
        except EOFError:
            break
