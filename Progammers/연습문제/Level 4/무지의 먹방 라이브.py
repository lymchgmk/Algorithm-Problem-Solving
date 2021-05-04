def solution(food_times, k):
    foods = [[food_times[idx], idx+1] for idx in range(len(food_times))]
    foods.sort()
    
    L = len(foods)
    pretime = 0
    for idx, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * L
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= L
                sublist = sorted(foods[idx:], key=lambda x: x[1])
                return sublist[k][1]
        L -= 1
    
    return -1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
