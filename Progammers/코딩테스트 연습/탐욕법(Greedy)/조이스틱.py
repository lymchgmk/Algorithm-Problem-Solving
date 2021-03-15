def solution(name):
    cnt = [min(26 - ord(i) + 65, ord(i) - 65) for i in name if i != 'A']
    idx = [i for i, v in enumerate(name) if v != 'A']

    graph = [idx[i + 1] - idx[i] for i in range(len(idx) - 1)] + [len(name) - idx[-1]]
    if name[0] == 'A':
        idx = [0] + idx
        graph = [idx[1]] + graph

    answer = [2 * sum(graph[:i]) + (len(name) - idx[i + 1]) for i, v in enumerate(idx) if 0 < v < len(name) // 2] + [
        idx[-1], len(name) - idx[1]]
    return sum(cnt) + min(answer)


name = "JAN"
print(solution(name))