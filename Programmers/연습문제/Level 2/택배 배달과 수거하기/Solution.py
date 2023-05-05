def solution(cap, n, deliveries, pickups):
    while deliveries and not deliveries[-1]:
        deliveries.pop()
    while pickups and not pickups[-1]:
        pickups.pop()

    answer = 0
    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2

        deliveries_cap = pickups_cap = cap
        while deliveries:
            if deliveries[-1] <= deliveries_cap:
                deliveries_cap -= deliveries.pop()
            else:
                deliveries[-1] -= deliveries_cap
                break
        while pickups:
            if pickups[-1] <= pickups_cap:
                pickups_cap -= pickups.pop()
            else:
                pickups[-1] -= pickups_cap
                break

    return answer


if __name__ == "__main__":
    cap = 4
    n = 5
    deliveries = [1, 0, 3, 1, 2]
    pickups = [0, 3, 0, 4, 0]
    print(solution(cap, n, deliveries, pickups)) # 16
