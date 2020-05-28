import sys
sys.stdin=open("1244_최대 상금.txt")

# 어차피 완전탐색 + 가지치기로 풀 수 있다면 / 그냥 무식하게 string으로 swap 구현해서 풀어도 될 것.
T = int(input())

for test_case in range(1, T+1):
    deck, swap = input().split()
    # 0번 'swap'된 경우
    solve = [deck]
    # 'swap'번 까지 swap 할 것 / 'swap' 완료 후마다 temp에 임시저장
    for i in range(int(swap)):
        temp = solve
        solve = []
        # 기준 정하기(swap_A), 마지막 한 칸은 제외
        for swap_A in range(len(deck) - 1):
            # swap할 대상 정하기(swap_B), swap_A + 1 부터 마지막 칸 포함
            for swap_B in range(swap_A + 1, len(deck)):

                for idx in range(len(temp)):
                    # temp에서 하나 골라서
                    sample = temp[idx]
                    # list slicing으로 sample[swap_A]랑 sample[swap_B]를 swap한 string을 만듦
                    sample = sample[:swap_A] + sample[swap_B] + sample[swap_A + 1:swap_B] + sample[swap_A] + sample[swap_B + 1:]
                    # 중복 제외하고 추가
                    if sample not in solve:
                        solve += [sample]
    # 최댓값 구해서 print
    answer = max(map(int, solve))
    print(f'#{test_case} {answer}')