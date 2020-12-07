import sys
sys.stdin = open('18231_파괴된 도시.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


N, M = map(int, input().split())
adj_list = [[i] for i in range(N+1)]
for _ in range(M):
    U, V = map(int, input().split())
    adj_list[U].append(V)
    adj_list[V].append(U)

K = int(input())
destroyed = set(map(int, input().split()))
answer = []
check = set()
for d in destroyed:
    if set(adj_list[d]).issubset(destroyed):
        answer.append(d)
        check.update(adj_list[d])
    
    if check == destroyed:
        print(len(answer))
        print(*answer)
        break

else:
    print(-1)