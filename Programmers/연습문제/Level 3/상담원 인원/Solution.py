from heapq import heappush, heappop
INF = float('inf')


def solution(k, n, reqs):
    consulting_type_count, mento_headcount, mentees = k, n, reqs
    min_total_waiting_time = INF
    for distributed_mentos in distribute_mentos(mento_headcount, consulting_type_count):
        min_total_waiting_time = min(min_total_waiting_time, calc_waiting_time(distributed_mentos, mentees))

    return min_total_waiting_time


def distribute_mentos(headcount, type_count):
    if headcount < type_count:
        return []

    result = []

    def _generate(curr_array, remain_number, remain_size):
        if remain_size == 0:
            result.append({_type: count for _type, count in enumerate(curr_array, start=1)})
        else:
            for i in range(1, remain_number - remain_size + 2):
                post_array = curr_array.copy()
                post_array.append(i)
                _generate(post_array, remain_number - i, remain_size - 1)

    _generate([], headcount, type_count)

    return result


def calc_waiting_time(mentos, mentees):
    waiting_queue = {i: [] for i in mentos}
    waiting_time = 0

    for start_time, consulting_time, consulting_type in mentees:
        end_time = start_time + consulting_time

        if mentos[consulting_type] <= len(waiting_queue[consulting_type]):
            finished_end_time, finished_start_time = heappop(waiting_queue[consulting_type])
            if finished_end_time > start_time:
                waiting_time += finished_end_time - start_time
                start_time = finished_end_time
                end_time = start_time + consulting_time

        heappush(waiting_queue[consulting_type], (end_time, start_time))

    return waiting_time


if __name__ == "__main__":
    k = 3
    n = 6
    reqs = [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]
    print(solution(k, n, reqs))
