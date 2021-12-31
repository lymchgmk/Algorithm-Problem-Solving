import sys
sys.stdin = open('2748_피보나치 수 2.txt', 'rt')

n = int(input())
fibo_list = [0, 1]
while len(fibo_list)<=90:
    fibo_list.append(fibo_list[-2] + fibo_list[-1])

print(fibo_list[n])
