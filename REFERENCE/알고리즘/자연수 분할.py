def distribute_mentos(headcount, type_count):
    if headcount < type_count:
        return []

    result = []

    def _generate(curr_array, remain, depth):
        if depth == 1:
            curr_array.append(remain)
            result.append({_type: count for _type, count in enumerate(curr_array, start=1)})
        else:
            for i in range(1, remain - depth + 2):
                post_array = curr_array.copy()
                post_array.append(i)
                _generate(post_array, remain - i, depth - 1)

    _generate([], headcount, type_count)

    return result


n = 5
m = 3
print(distribute_mentos(4, 3))