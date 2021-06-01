import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    try:
        while scoville[0] < K:
            dish_1 = heapq.heappop(scoville)
            dish_2 = heapq.heappop(scoville)
            new_dish = dish_1 + (dish_2 * 2)
            heapq.heappush(scoville, new_dish)
            answer += 1
            
    except IndexError:
        answer = -1
    
    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
