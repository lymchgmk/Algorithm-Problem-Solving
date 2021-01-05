import sys
sys.stdin = open('10757_큰 수 A+B.txt', 'rt')


A, B = map(int, sys.stdin.readline().split())
print(A + B)