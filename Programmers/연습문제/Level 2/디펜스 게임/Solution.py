def solution(n, k, enemy):
    left, right = 0, enemy.len

    while left < right:
        mid = (left + right) / 2

        currEnemy = enemy[:mid+1]
        if canDefense(n, k, currEnemy):
            left = mid + 1
        else:
            right = mid

    return left

def canDefense(n, k, currEnemy):
    import heapq



n = 7
k = 3
print(solution(n, k, enemy))