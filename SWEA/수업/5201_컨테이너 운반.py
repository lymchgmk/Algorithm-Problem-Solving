import sys
sys.stdin=open("5201_컨테이너 운반.txt")

# 무거운 화물부터,
# 화물을 옮길 수 있는 트럭 중 가장 가벼운 트럭이 옮기면 된다.

T=int(input())

for test_case in range(1, T+1):
    N, M=map(int, input().split())
    wi=list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort()

    result=0
    while wi:
        weight=wi.pop(0)
        for truck in ti:
            if truck >= weight:
                result+=weight
                ti.remove(truck)
                break

    print(f'#{test_case} {result}')