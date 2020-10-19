import sys
sys.stdin = open('1085_직사각형에서 탈출.txt', 'rt')


x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))
