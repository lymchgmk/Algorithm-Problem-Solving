#1. DFS로 k개 조합 생성
def combine_1(self, n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()

    dfs([], l, k)
    return results


#2. itertools 모듈 사용
import itertools


def combine_2(self, n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, N+1), k))
