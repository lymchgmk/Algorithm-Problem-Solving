import sys
sys.stdin = open("14888_연산자 끼워넣기.txt", "rt")


from itertools import permutations


N = int(input())
A = list(map(int, sys.stdin.readline().split()))
# + - * /
N = list(map(int, sys.stdin.readline().split()))

