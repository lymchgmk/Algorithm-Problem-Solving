import sys
sys.stdin = open('전기버스.txt', 'r')

def whatthebus(my_K, my_bus_will_stop):
    bus_start = 0
    charged_max = my_K
    charge_count = 0

    while True:
        max_K_check = 0
        for i in range(bus_start + 1, charged_max + 1):
            if my_bus_will_stop[i] == 1:
                bus_start = i
            else:
                max_K_check += 1

        if max_K_check == my_K:
            return 0

        charge_count += 1
        charged_max = bus_start + my_K

        if charged_max >= N:
            return charge_count

T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_charge = list(map(int, input().split()))

    bus_will_stop = [0 for _ in range(N+1)]
    for i in range(len(bus_charge)):
        bus_will_stop[bus_charge[i]] = 1

    print(f'#{test_case} {whatthebus(K, bus_will_stop)}')