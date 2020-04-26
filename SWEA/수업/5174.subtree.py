# 부모없는=루트노드 찾기
# 루트->후보로 이동 후
# 후보에서 다시 dfs->visited에 없는거따라 내려감
# count 후 리턴

import sys
sys.stdin = open('5174.subtree.txt')

def dfs(start, graph):
    visit=[]
    stack=[]

    stack.append(start)

    while stack:
        node=stack.pop()
        if node==0:
            break
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


T=int(input())

for test_case in range(1, T+1):
    E, N=map(int, input().split())
    data=list(map(int, input().split()))
    mat=[[] for _ in range(E+2)]
    for i in range(len(data)):
        if i%2==0:
            mat[data[i]].append(data[i+1])

    ans=len(dfs(N, mat))
    print(f'#{test_case} {ans}')