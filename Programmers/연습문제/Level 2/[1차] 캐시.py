def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    answer = 0
    
    for city in cities:
        city = city.lower()
        if not city in cache:
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer



cacheSize = 2
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))