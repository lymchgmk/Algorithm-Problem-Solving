import sys
sys.stdin = open('1427_소트인사이드.txt', 'rt')

print(''.join(sorted(input(), reverse=True)))