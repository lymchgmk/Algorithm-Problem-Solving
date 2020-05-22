import sys
from itertools import combinations
from collections import deque
sys.stdin=open('16637_괄호추가하기.txt')

N = int(input())

expression = input()
answer = -2 ** 31

operators = ["+", "-", "*"]
my_operators=[]
my_numbers=[]

for char in expression:
    if char in operators:
        my_operators.append(char)
    else:
        my_numbers.append(char)

test=[]
for i in range(len(my_operators)):
    for combination in combinations(range(len(my_operators)), i):
        temp=list(combination)
        sample=[]
        for i in range(1, len(temp)):
            sample.append(temp[i]-temp[i-1])
        if 1 not in sample:
            test.append(temp)
print(expression)
print(my_numbers)
print(my_operators)
print(test)

result=deque()
# 이걸 어떻게 구현할까




