#import sys
#sys.stdin = open("Algo2_구미_1반_임창묵.txt")

from itertools import permutations

# 0. 문제에서 주어진 데이터 값 입력받음.
T = int(input())
for test_case in range(1, T+1):
    # 0-1. N : 어린이 수 / M : 사탕 종류
    N, M = map(int, input().split())
    kids = [list(map(int, input().split())) for _ in range(N)]

    # 0-2. 문제 조건에서 사탕 종류(M)이 어린이(N)보다 적은 경우에는 M명의 어린이만 나눠 준다고 했으므로.
    if M < N:
        # 0-2. (N-M)명의 어린이들이 가진 사탕 종류의 수는 마지막에 보정해 줄 예정.
        extra_kids = kids[M:]
        kids = kids[:M]

    K = len(kids)

    candies = list(range(1, M+1))
    # 1. 1<=N<=10, 1<=M<=10 이므로 permutations를 사용한 완전탐색 + 가지치기 사용해도 괜찮다고 판단.
    give_candies = permutations(candies, K)

    # 2. 아이들이 보유하고 있지 않은 사탕의 set을 나타낼 candy_needs 변수 생성.
    candy_needs = []
    answer = 0
    for kid in kids:
        # 2-1. kid[0]은 현재 아이가 가지고 있는 사탕의 총 갯수이므로 필요없어서 slicing 후 사용.
        # 3. 현재 아이들이 가지고 있는 중복되지 않은 사탕의 종류를 answer로 나타냄. 이후에 answer에 늘어난 사탕의 종류를 더해서 최종 답을 만들 것.
        answer += len(list(set(kid[1:])))
        # 2-2. set을 사용해서 중복 배제.
        candy_needs.append(set(candies)-set(kid[1:]))

    # 3. 증가한, 중복되지 않은 사탕의 종류를 result로 나타냄.
    result = 0
    # 3-1. permutations로 만든 완전탐색의, 아이들에게 줄 사탕의 종류인 give.
    for give in give_candies:
        # 3-2. give마다 결정되는 (증가한, 중복되지 않은 사탕의 종류를) sub_result를 임시저장.
        sub_result = 0
        for i in range(K):
            if give[i] in candy_needs[i]:
                # 3-3. 사탕 줌.
                sub_result += 1
        # 3-3. sub_result 중 최대의 값을 result에 옮김.
        if result <= sub_result:
            result = sub_result
        # 3-4. 가지치기, sub_result 값은 len(kids)의 값을 넘을 수 없으므로.
        if result == K:
            break

    # 4. (N-M)명의 어린이들, extra_kids가 가진 사탕 종류의 수를 마지막에 보정.
    if M < N:
        for kid in extra_kids:
            answer += len(list(set(kid[1:])))

    # 5. 출력
    answer += result
    print(f'#{test_case} {answer}')
