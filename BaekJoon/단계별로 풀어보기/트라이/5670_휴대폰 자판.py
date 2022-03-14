import sys
from collections import defaultdict
sys.stdin = open("5670_휴대폰 자판.txt", "rt")


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.size = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        for word in words:
            node = self.root
            for char in word:
                node = node.children[char]
                node.size += 1

    def count_buttons(self, word):
        curr_node = self.root
        cnt = 0
        for char in word:
            post_node = curr_node.children[char]
            if curr_node.size != post_node.size:
                cnt += 1
            curr_node = post_node
        return cnt


def solution(N, words):
    trie = Trie()
    trie.insert(words)
    button_cnt = sum(trie.count_buttons(word) for word in words)
    answer = round(button_cnt / len(words), 2)
    print(f'{answer:.2f}')


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    while True:
        N = input()
        if not N:
            break
        words = [input() for _ in range(int(N))]
        solution(N, words)
