def solution(N, stations, W):
    import math
    
    dist = []
    for i in range(1, len(stations)):
        dist.append((stations[i]-W-1)-(stations[i-1]+W))
    dist.append(stations[0]-W-1)
    dist.append(N-(stations[-1]+W))
    
    answer = 0
    for d in dist:
        if d > 0:
            answer += math.ceil(d / (2*W+1))
    return answer


N = 16
stations = [9]
W = 2
print(solution(N, stations, W))
# 3
