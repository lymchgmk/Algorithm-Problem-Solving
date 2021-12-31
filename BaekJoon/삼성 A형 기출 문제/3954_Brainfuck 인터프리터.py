import sys
sys.stdin=open("3954_Brainfuck 인터프리터.txt")

t=int(input())

for test_case in range(t):
    Sm=list(map(int, input().split()))
    Sc=list(input())
    Si=list(input())

    print(Sm, Sc, Si)