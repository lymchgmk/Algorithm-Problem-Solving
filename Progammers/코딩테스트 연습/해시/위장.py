import sys
sys.stdin = open('위장.txt')

from collections import Counter
from functools import reduce

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution1(clothes):
    cnt = Counter([kind for name, kind in clothes])
    print(cnt.values())
    answer = reduce(lambda x, y: x*(y+1), cnt.values()) - 1
    return answer

print(solution1(clothes))