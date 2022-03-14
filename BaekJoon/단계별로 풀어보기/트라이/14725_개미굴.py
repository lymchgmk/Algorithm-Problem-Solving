import sys
from collections import defaultdict
sys.stdin = open("14725_개미굴.txt", "rt")


class Node:
    def __init__(self):
        self.end = False
        self.children = defaultdict(Node)


class AntTree:
    def __init__(self):
        self.root = Node()

    def insert(self, foods):
        node = self.root
        for food in foods:
            node = node.children[food]
        node.end = True

    def traversal(self, level, node):
        if node.end:
            return

        for child in sorted(node.children):
            print("--"*level + child)
            self.traversal(level+1, node.children[child])


def solution(N, foods):
    ant_tree = AntTree()
    for foods in foods_list:
        ant_tree.insert(foods)
    ant_tree.traversal(0, ant_tree.root)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    foods_list = []
    for _ in range(N):
        K, *foods = input().split()
        foods_list.append(foods)
    solution(N, foods_list)
