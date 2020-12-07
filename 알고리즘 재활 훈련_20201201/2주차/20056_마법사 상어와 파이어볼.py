import sys
sys.stdin = open('20056_마법사 상어와 파이어볼.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


def subset(lst):
    L = len(lst)
    result = []
    for i in range(1<<L):
        for j in range(L):
            temp = [x for x in lst if i & (1 << j)]
            print(temp)