import sys
sys.stdin = open('1874_스택 수열.txt', 'rt')

n = int(input())
count = 0
stack, result = [], []
flag = True

for _ in range(n):
    num = int(input())

    while count < num:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    print(*result, sep = "\n")



# from sys import stdin
# input()
# n,s,p=0,[],[]
# for i in map(int, stdin):
#     if s and s[-1]>i:print('NO');exit()

#     while not s or s[-1]<i:
#         n+=1
#         s.append(n)
#         p.append('+')

#     s.pop()
#     p.append('-')

# print('\n'.join(p))
