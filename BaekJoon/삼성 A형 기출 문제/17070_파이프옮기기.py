import sys
from _collections import deque
sys.stdin=open('17070_파이프옮기기.txt')

def issafe(node, data):
    if (0<=node[0]<N and 0<=node[1]<N) and data[node[0]][node[1]]==0:
        return True
    else:
        return False

def bfs(start, data):
    global count
    dirs_sample = [(0, 1, 0), (1, 0, 1), (1, 1, 2)]
    queue=deque()
    queue.append(start)

    while queue:
        temp=queue.pop()

        if temp[2]!=2:
            dirs = [dirs_sample[temp[2]], dirs_sample[2]]
        else:
            dirs=dirs_sample

        for dir in dirs:
            test = [temp[0] + dir[0], temp[1] + dir[1], dir[2]]

            if test[2]==2:
                if issafe([test[0]-1, test[1], test[2]], data) and issafe([test[0], test[1]-1, test[2]], data):
                    if [test[0], test[1]] == [N-1,N-1]:
                        count += 1
                    else:
                        queue.append(test)

            else:
                if issafe(test, data):
                    if [test[0], test[1]] == [N - 1, N - 1]:
                        count += 1
                    else:
                        queue.append(test)

N=int(input())

data=[list(map(int, input().split())) for _ in range(N)]

count=0
start=(0,1,0) # 가로:0 / 세로:1 / 대각선:2

bfs(start, data)

print(count)