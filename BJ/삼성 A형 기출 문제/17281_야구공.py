import sys
sys.stdin=open("17281_야구공.txt")

inning=int(input())
batters=[list(map(int, input().split())) for _ in range(inning)]

bases=[0]*4

point=0
out=0
while out != 3:
