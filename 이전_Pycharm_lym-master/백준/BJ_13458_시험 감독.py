import sys
import math
sys.stdin = open("BJ_13458_시험 감독.txt")

N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

students = [num-B for num in Ai]

result = [math.ceil(student/C) for student in students if student > 0]

print(sum(result)+N)