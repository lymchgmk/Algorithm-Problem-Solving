import sys
sys.stdin = open("5521_상원이의 생일파티.txt")

T=int(input())
for test_case in range(1, T+1):
    N,M=map(int, input().split())

    adj_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        adj_matrix[a][b] = 1
        adj_matrix[b][a] = 1

    answer=set()
    for idx_1, val_1 in enumerate(adj_matrix[1]):
        if idx_1 != 1 and val_1 != 0:
            answer.add(idx_1)
            for idx_2, val_2 in enumerate(adj_matrix[idx_1]):
                if idx_2 != 1 and val_2 != 0:
                    answer.add(idx_2)
    answer = len(list(answer))
    print(f'#{test_case} {answer}')


