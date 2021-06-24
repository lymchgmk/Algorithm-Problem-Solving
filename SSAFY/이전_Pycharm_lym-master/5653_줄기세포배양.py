import sys
sys.stdin = open("5653_줄기세포배양.txt", "r")
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N, M, K = map(int, input().split())
#     cell =[]
#     for line in range(N):
#         cell.append(list(map(int, input().split())))
#
# #    print(N, M, K)
# #    print(cell)
#
# # 죽은 활성 비활성을 진수 차이로 표기해서 메커니즘 짜볼것
# # 세포 번식 후 어떻게?

# 답안
# D=[1,-1,0,0]
# for T in range(int(input())):
#     N,M,K=map(int, input().split());S=[[0]*(2*K+M)for i in range(K)]; U=[];A=[]
#     for y in range(N):
#         S+=[[0]*K+list(map(int,input().split()))+[0]*K]
#         for x in range(2*K+M):
#             if S[y+K][x]:U+=[[y+K,x,S[y+K][x]]]
#     S+=[[0]*(2*K+M)for i in range(K)]
#     for t in range(K):
#         for Y,X,_ in A:
#             for d in range(4):
#                 y=Y+D[d];x=X+D[d-2]
#                 if not S[y][x]:S[y][x]=S[Y][X];U+=[[y,x,S[Y][X]+1]]
#         A=list(filter(lambda x:x[2]>0, map(lambda x:[*x[:2],x[2]-1],A)));U=list(map(lambda x:[*x[:2],x[2]-1],U));A+=list(map(lambda x:[*x[:2],S[x[0]][x[1]]],filter(lambda x:x[2]==0,U)));U=list(filter(lambda x:x[2]>0,U))
#     print("#%d"%(T+1),len(A)+len(U))
#
#
# #답안 들여쓰기 버전
# D = [1, -1, 0, 0]
#
# for T in range(int(input())):
#     N, M, K = map(int, input().split())
#     S = [[0] * (2 * K + M) for i in range(K)]
#     U = []
#     A = []
#
#     for y in range(N):
#         S += [[0] * K + list(map(int, input().split())) + [0] * K]
#         for x in range(2 * K + M):
#             if S[y + K][x]:
#                 U += [[y + K, x, S[y + K][x]]]
#
#     S += [[0] * (2 * K + M) for i in range(K)]
#
#     for t in range(K):
#         for Y, X, _ in A:
#             for d in range(4):
#                 y = Y + D[d]
#                 x = X + D[d - 2]
#                 if not S[y][x]:
#                     S[y][x] = S[Y][X]
#                     U += [[y, x, S[Y][X] + 1]]
#
#         A = list(filter(lambda x: x[2] > 0, map(lambda x: [*x[:2], x[2] - 1], A)))
#         U = list(map(lambda x: [*x[:2], x[2] - 1], U))
#         A += list(map(lambda x: [*x[:2], S[x[0]][x[1]]], filter(lambda x: x[2] == 0, U)))
#         U = list(filter(lambda x: x[2] > 0, U))
#
#     print("#%d" % (T + 1), len(A) + len(U))

# 다른 답안

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

testcase = int(input())

for test in range(testcase):
    N, M, K = map(int, input().split())
    NM_matrix = [list(map(int, input().split())) for i in range(N)]
    final_matrix = [[0] * (M + K) for i in range(N + K)]
    cell_list = [[] for i in range(10 + 1)] # 생명력 : 1<= X <= 10

    for i in range(N):
        for j in range(M):
            if NM_matrix[i][j] > 0:
                cell_life = NM_matrix[i][j]
                final_matrix[i + K // 2][j + K // 2] = cell_life
                cell_list[cell_life].append((i + K // 2, j + K // 2))

    for time in range(1, K + 1):

        for v in range(10, 0, -1):
            if time % (v + 1) != 0:
                continue
            survive_cells = []

            for c in cell_list[v]:
                if (K - time) < (v - 1):
                    survive_cells.append(c)

                for i in range(4):
                    if final_matrix[c[0] + dy[i]][c[1] + dx[i]] == 0:
                        final_matrix[c[0] + dy[i]][c[1] + dx[i]] = v
                        survive_cells.append((c[0] + dy[i], c[1] + dx[i]))
            cell_list[v] = survive_cells

    print("#{} {}".format(test + 1, sum(len(c) for c in cell_list)))

