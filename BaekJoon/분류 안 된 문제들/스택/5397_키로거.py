import sys
sys.stdin = open("5397_키로거.txt", "rt")


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.post = None


class MyDoubleLinkedList:
    def __init__(self):
        self.head, self.tail = Node(None), Node(None)
        self.head.post, self.tail.prev = self.tail, self.head
        self.cursor = 0

    def length(self):
        _length, curr = 0, self.head
        while curr.post:
            curr = curr.post
            _length += 1
        return _length

    def move_cursor(self, char):
        if char == '<':
            self.cursor = max(0, self.cursor - 1)
        elif char == '>':
            self.cursor = min(self.length(), self.cursor + 1)

    def insert_at(self, char):
        curr = self.head
        for _ in range(self.cursor):
            curr = curr.post
        post = curr.post

        insert_node = Node(char)
        curr.post = post.prev = insert_node
        insert_node.prev, insert_node.post = curr, post

    def pop_at(self):
        curr = self.head
        for _ in range(self.cursor):
            curr = curr.post
        prev, post = curr.prev, curr.post
        prev.post, post.prev = post, prev
        self.cursor -= 1

    def print(self):
        curr = self.head
        while curr.post.data != None:
            print(curr.data, end=' ')


def solution(string):
    mdll = MyDoubleLinkedList()
    for char in string:
        print(mdll.cursor)
        if char in ('<', '>'):
            mdll.move_cursor(char)
        elif char == '-':
            mdll.pop_at()
        else:
            mdll.insert_at(char)
        print(mdll.cursor)
    mdll.print()


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        string = input()
        solution(string)
