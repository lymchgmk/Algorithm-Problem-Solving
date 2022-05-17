from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    deq = deque([0]*bridge_length, maxlen=bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    while deq:
        bridge_weight -= deq.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                left_truck = truck_weights.popleft()
                bridge_weight += left_truck
                deq.append(left_truck)
            else:
                deq.append(0)
        answer += 1
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))