from typing import List
import itertools
import collections


# 풀이 1. DFS로 순환 구조 판별
def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        
        traced.add()
        for y in graph[i]:
            if not dfs(y):
                return False
            
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)

        return True
    
    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
        
    return True


# 풀이 2. 가지치기를 이용한 최적화
def canFinish_2(self, numCourses: int, prerequisited: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisited:
        graph[x].append(y)
    
    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 아미 방문했던 노드이면 False
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)
    
        return True

    
    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    
    return True