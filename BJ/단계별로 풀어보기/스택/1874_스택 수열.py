import sys
sys.stdin = open('1874_스택 수열.txt', 'rt')


n = int(input())
seq = [int(input()) for _ in range(n)]
stack, result, answer = [1], [], ["+"]
num, idx = 2, 0
while stack:
    if n == 1:
        result.append(1)
        answer.append("-")
        break

    if seq[idx] != stack[-1]:
        stack.append(num)
        num += 1
        answer.append("+")
    else:
        temp = stack.pop()
        result.append(temp)
        idx += 1
        answer.append("-")
    
    if not stack and seq[idx] == num:
        stack.append(num)
        answer.append("+")
        num += 1
        idx += 1
    
print(num, idx, seq[idx])
print(stack, result, answer)

if result == seq:
    print(*answer, sep = "\n")
else:
    print("NO")


    

