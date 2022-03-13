import sys
from collections import defaultdict
sys.stdin = open("5052_전화번호 목록.txt", "rt")


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.word or char not in node.children:
                return False
            node = node.children[char]
        return True


def solution(numbers):
    numbers.sort(key=lambda x: len(x))

    trie = Trie()
    for number in numbers:
        trie.insert(number)
        if not trie.starts_with(number):
            return "NO"
    return "YES"


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    T = int(input())
    for _ in range(T):
        N = int(input())
        phone_numbers = [input() for _ in range(N)]
        print(solution(phone_numbers))
