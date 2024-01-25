from collections import defaultdict, Counter


DONUT, ROD, EIGHT = 1, 2, 3


def solution(edges):
    graph = defaultdict(list)
    counter = Counter()
    for s, e in edges:
        graph[s].append(e)
        counter[s] += 1

    root_v = counter.most_common()[0][0]
    answer = [root_v, 0, 0, 0]
    for start_v in graph[root_v]:
        result = find_cycle(start_v, graph)
        answer[result] += 1

    return answer


def find_cycle(start_v, graph):
    stack = [start_v]
    visited_count = defaultdict(int)
    path = []
    while stack:
        curr_v = stack.pop()
        visited_count[curr_v] += 1
        path.append(curr_v)

        for post_v in graph[curr_v]:
            if visited_count[post_v] == 0:
                stack.append(post_v)
            else:
                visited_count[post_v] += 1

    count_start_or_cross = sum(visited_count.values()) - len(visited_count.keys())

    if count_start_or_cross == 0:
        return ROD
    elif count_start_or_cross == 1:
        return DONUT
    else:
        return EIGHT


if __name__ == "__main__":
    edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    # edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
    result = [4, 0, 1, 2]
    my_answer = solution(edges)
    print(f"my_answer: {my_answer}")
    print(f"{result == my_answer}")
