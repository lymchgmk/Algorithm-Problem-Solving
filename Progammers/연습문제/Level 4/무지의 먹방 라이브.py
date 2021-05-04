def solution(food_times, k):
    foods = [[food_times[idx], idx+1] for idx in range(len(food_times))]
    foods.sort()

    L = len(foods)
    _min = 0
    for idx, food in enumerate(foods):
        diff = food[0] - _min
        if diff != 0:
            edible = diff * L
            if edible <= k:
                k -= edible
                _min = food[0]
            else:
                remain_foods = sorted(foods[idx:], key=lambda x: x[1])
                return remain_foods[k % L][1]
        L -= 1

    return -1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
