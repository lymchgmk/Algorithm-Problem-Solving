from collections import defaultdict


def solution(land, height):
    def DFS(land, height):
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        marked_land = [[0] * N for _ in range(N)]
        mark_num = 1
        ladders_dict = defaultdict(lambda: float('inf'))
ly
                        curr_x, curr_y, curr_h = stack.pop()
                        for dir_x, dir_y in dirs:
                            post_x, post_y = curr_x + dir_x, curr_y + dir_y
                            if 0 <= post_x < N and 0 <= post_y < N:
                                post_h = land[post_x][post_y]
                                if marked_land[post_x][post_y] == 0 and abs(curr_h - post_h) <= height:
                                    stack.append((post_x, post_y, post_h))
                                    marked_land[post_x][post_y] = mark_num
                                elif marked_land[post_x][post_y] not in (0, mark_num):
                                    curr_m, post_m = marked_land[curr_x][curr_y], marked_land[post_x][post_y]
                                    ladders_dict[(curr_m, post_m)] = min(ladders_dict[(curr_m, post_m)], abs(curr_h - post_h))
                    mark_num += 1
        return mark_num, marked_land, ladders_dict

    def MST(V, ladders):
        V -= 1
        adj = [[0] * V for _ in range(V)]
        for (s, e), c in ladders.items():
            adj[s-1][e-1] = c
            adj[e-1][s-1] = c

        INF = float('inf')
        key = [INF] * V
        p = [-1] * V
        mst = [False] * V

        key[0] = 0
        cnt = 0
        result = 0
        while cnt < V:
            min = INF
            u = -1
            for i in range(V):
                if not mst[i] and key[i] < min:
                    min = key[i]
                    u = i

            mst[u] = True
            result += min
            cnt += 1

            for w in range(V):
                if 0 < adj[u][w] < key[w] and not mst[w]:
                    key[w] = adj[u][w]
                    p[w] = u
        return result

    N = len(land)
    mark_num, marked_land, ladders_dict = DFS(land, height)
    return MST(mark_num, ladders_dict)


# import heapq
#
#
# def solution(land, height):
#     N = len(land)
#
#     # 방문 여부를 체크하는 2차원 배열
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#     # 큐
#     queue = []
#
#     visit_count = 0
#     max_count = N * N
#     value = 0
#
#     # 탐색 시작 지점을 큐에 넣는다.
#     queue.append((0, 0, 0))
#
#     while visit_count < max_count:
#         print(queue)
#         # 사다리비용, x좌표, y좌표
#         val, x, y = heapq.heappop(queue)
#
#         # 이미 방문한 곳이라면 건너뛴다.
#         if visited[x][y]:
#             continue
#         visited[x][y] = True
#
#         visit_count += 1
#         value += val
#
#         # 현재 칸의 높이
#         current_height = land[x][y]
#
#         for dx, dy in move:
#             nx, ny = x + dx, y + dy
#
#             if nx < 0 or ny < 0 or nx >= N or ny >= N:
#                 continue
#
#             # 다음 칸의 높이
#             next_height = land[nx][ny]
#
#             # 현재 칸과 다음 칸의 높이 차이가 height보다 크다면 사다리가 필요한 시점
#             if abs(next_height - current_height) > height:
#                 heapq.heappush(
#                     queue, (abs(next_height - current_height), nx, ny))  # (사다리비용, x좌표, y좌표)
#             # 사다리가 필요하지 않은 시점은 사다리비용을 0으로 처리
#             # 다음 반복문에서 value += 0 이기 때문에 결과값에 영향을 미치지 않음
#             else:
#                 heapq.heappush(queue, (0, nx, ny))
#     return value


if __name__ == "__main__":
    land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
    height = 3
    print(solution(land, height)) # 15
    
    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    height = 1
    print(solution(land, height)) # 18
