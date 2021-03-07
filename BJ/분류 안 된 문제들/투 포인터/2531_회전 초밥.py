import sys
sys.stdin = open('2531_회전 초밥.txt', 'r')


input = lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())
T = list(map(int, input().split()))