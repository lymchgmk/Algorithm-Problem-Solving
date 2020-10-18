def W_chairman(floor, room):
    if room == 1:
        return 1
        
    if floor == 0:
        return room
    elif floor == 1:
        return int(room * (room + 1) / 2)
    else:
        return W_chairman(floor-1, room) + W_chairman(floor, room-1)

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    print(W_chairman(k, n))