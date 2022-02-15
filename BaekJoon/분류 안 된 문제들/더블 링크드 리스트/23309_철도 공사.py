import sys
sys.stdin = open("23309_철도 공사.txt", "rt")


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.prev = self.head.next = self.head

    def insert(self, default_numbers_lst):
        curr = self.head
        for dn in default_numbers_lst:
            node = Node(dn)
            if self.head.data is None:
                self.head = node
                self.head.prev = self.head.next = node
            else:
                next = curr.next
                next.prev, node.next = node, next
                curr.next, node.prev = node, curr
            curr = curr.next

    def build(self, _command, _numbers):
        curr = self.head
        while True:
            if curr.data == _numbers[0]:
                break
            curr = curr.next

        node = Node(_numbers[1])
        if _command == "BN":
            target = curr.next
            prev, next = curr, target
        else:
            target = curr.prev
            prev, next = target, curr
        print(target.data)
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def close(self, _command, _numbers):
        curr = self.head
        while True:
            if curr.data == _numbers[0]:
                break
            curr = curr.next

        if _command == "CN":
            target = curr.next
        else:
            target = curr.prev
        print(target.data)
        prev, next = target.prev, target.next
        prev.next, next.prev = next, prev

    def print(self):
        curr = self.head.next
        print("print")
        while curr.data is not None:
            print(curr.data)
            curr = curr.next


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    CLL = CircularLinkedList()
    default_numbers = input().split()
    CLL.insert(default_numbers)
    for _ in range(M):
        command, *numbers = input().split()
        print(numbers)
        if command in ("BN", "BP"):
            CLL.build(command, numbers)
        else:
            CLL.close(command, numbers)
        CLL.print()
        print()