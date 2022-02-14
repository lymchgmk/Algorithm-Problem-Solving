import sys
sys.stdin = open("5397_키로거.txt", "rt")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.cursor = 0

    def move(self, char):
        if char == '<':
            if self.cursor != 0:
                self.cursor -= 1
        elif char == '>':
            if self.cursor != self.length:
                self.cursor += 1

    def add(self, char):



def solution(str_L):




if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        str_L = input()
        solution(str_L)
