# 숫자 리스트, 연산자 리스트, 계산 후 리스트 만들어서
# 연산자 리스트는 중복 제외한 순열로 추출 = 조합 후 순열 후 리스트 넣어서\
# 리스트에서 뽑아서 돌리면서
# 숫자랑 이터러블하게 곱해서 min, max 구하기
# 중복 제외 순열이 제일 문제 일 듯



from itertools import combinations
from itertools import permutations
import sys
sys.stdin = open("BJ_14888_연산자 끼워넣기.txt")


N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

op_list = []
