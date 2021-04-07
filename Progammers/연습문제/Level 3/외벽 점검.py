from collections import deque


def solution(n, weak, dist):
    # 내림차순 정렬
    dist.sort(reverse=True)
    # popleft 사용
    deq = deque([weak])
    # 이미 검사 했는지 안했는지 체크
    visited = set(tuple(weak))
    # dist 순회
    for idx, dst in enumerate(dist):
        # 이러면 기존 deq 다 빼고 다시 반복
        for _ in range(len(deq)):
            # 검사할 데이터 뽑고
            current = deq.popleft()
            # 검사 조회
            for cur in current:
                # fix 할 수 없는 것들을 temp로 저장
                left, right = cur, (cur + dst) % n
                if left < right:
                    temp = tuple(filter(lambda x: x < left or x > right, current))
                else:
                    temp = tuple(filter(lambda x: x < left and x > right, current))
                
                # 다 fix 가능한 경우
                if len(temp) == 0:
                    return idx + 1
                else:
                    if temp not in visited:
                        visited.add(temp)
                        deq.append(temp)
    return -1


# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]
3
print(solution(n, weak, dist))
