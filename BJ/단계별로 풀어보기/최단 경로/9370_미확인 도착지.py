import sys
sys.stdin = open("9370_미확인 도착지.txt", "rt")
input = lambda: sys.stdin.readline().strip()
import heapq


def dijkstra():
    pass


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    dist = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        adj

    for _ in range(t):
        x = int(input())