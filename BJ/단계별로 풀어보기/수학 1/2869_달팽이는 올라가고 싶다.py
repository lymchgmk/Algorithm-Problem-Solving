import sys
import math
sys.stdin = open('2869_달팽이는 올라가고 싶다.txt', 'rt')

A, B, V = map(int,input().split())
d = (V-B)/(A-B)
print(int(d) if d == int(d) else int(d)+1)

# 이게 왜 시간초과가 나지;
# PyPy3는 시간초과 / Python3는 통과
