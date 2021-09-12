import sys
sys.stdin = open("12784_인하니카 공화국.txt", "r")
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)


T = int(input())
ROOT = 1
for _ in range(T):
    N, M = map(int, input().split())
    adj = {i: {} for i in range(1, N+1)}
    for _ in range(M):
        S, E, D = map(int, input().split())
        adj[S][E] = D
        adj[E][S] = D

    tree = {i: {} for i in range(1, N+1)}
    visited =
    stack = [ROOT]
    while stack:
        curr = stack.pop()





