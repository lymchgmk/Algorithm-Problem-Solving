import sys
sys.stdin = open('3009_네 번째 점.txt', 'rt')


x_dict, y_dict = dict(), dict()
for _ in range(3):
    x, y = map(int, input().split())
    if x not in x_dict.keys():
        x_dict[x] = 1
    else:
        x_dict[x] += 1
    if y not in y_dict.keys():
        y_dict[y] = 1
    else:
        y_dict[y] += 1

result = []
for x_key in x_dict.keys():
    if x_dict[x_key] == 1:
        result.append(x_key)
for y_key in y_dict.keys():
    if y_dict[y_key] == 1:
        result.append(y_key)

print(*result)


