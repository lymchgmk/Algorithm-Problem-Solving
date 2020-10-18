import sys
import re
import math
sys.stdin = open('test.txt', 'rt')


X = int(input())

idx = math.ceil((2*X+0.25)**0.5 - 0.5)
seq = X - idx*(idx-1)//2
if idx % 2 == 1:
    print(f'{idx-seq+1}/{seq}')
else:
    print(f'{seq}/{idx-seq+1}')
