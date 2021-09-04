# def solution(land, P, Q):
#     def count_cost(height):
#         cost = 0
#         for i in range(N):
#             for j in range(N):
#                 if land[i][j] > height:
#                     cost += (land[i][j] - height) * Q
#                 else:
#                     cost += (height - land[i][j]) * P
#         return cost
#
#     N = len(land)
#     l, h = min(min(land)), max(max(land))
#     answer = 0
#     while l <= h:
#         m = (l + h) // 2
#         l_cost, h_cost = count_cost(m), count_cost(m+1)
#         if l_cost > h_cost:
#             answer = h_cost
#             l = m + 1
#         else:
#             answer = l_cost
#             h = m - 1
#     return answer


def solution(land, P, Q):
    flat_land = [block for floor in land for block in floor]
    flat_land.sort()
    N = len(flat_land)
    block_increase = -1
    prev_blocks, total_blocks = 0, sum(flat_land)
    answer = float('inf')
    for i in range(N):
        blocks = flat_land[i]
        if block_increase != blocks:
            cost = (blocks * i - prev_blocks) * P + (total_blocks - prev_blocks - (N - i) * blocks) * Q
            if cost < answer:
                answer = cost
                block_increase = blocks
        prev_blocks += blocks
    return answer


def solution(land, P, Q):
    floors = sum(land, [])
    floors.sort()
    N = len(land)
    height = int(N*N*Q / (Q+P))
    layer = floors[height]
    answer = 0
    for floor in floors:
        if floor < layer:
            answer += (layer - floor) * P
        else:
            answer += (floor - layer) * Q
    return answer


if __name__ == "__main__":
    land = [[1, 2], [2, 3]]
    P, Q = 3, 2
    print(solution(land, P, Q))

    land = [[4, 4, 3], [3, 2, 2], [2, 1, 0]]
    P, Q = 5, 3
    print(solution(land, P, Q))
