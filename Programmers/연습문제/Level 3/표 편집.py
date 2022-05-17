def solution(n, k, cmd):
    class Node:
        def __init__(self, myself, before=None, after=None, is_deleted=False):
            self.myself = myself
            self.before = before
            self.after = after
            self.is_deleted = is_deleted

    # dummy
    table = {-1: Node(-1, before=n - 1, after=1)}

    # table 채우기
    for i in range(n):
        table[i] = Node(i, before=i - 1, after=i + 1)

    # table tail 처리
    table[n - 1].after = -1

    curr_cell = table[k]
    deleted_stack = []
    for c in cmd:
        operations = c.split()
        if operations[0] == 'U':
            _up = int(operations[1])
            while _up and curr_cell.before != -1:
                curr_cell = table[curr_cell.before]
                _up -= 1

        elif operations[0] == 'D':
            _down = int(operations[1])
            while _down and curr_cell.after != -1:
                curr_cell = table[curr_cell.after]
                _down -= 1

        elif operations[0] == 'C':
            prev_cell, post_cell = table[curr_cell.before], table[curr_cell.after]
            prev_cell.after, post_cell.before = curr_cell.after, curr_cell.before

            deleted_stack.append(curr_cell.myself)
            curr_cell.is_deleted = True

            if curr_cell.after != -1:
                curr_cell = post_cell
            else:
                curr_cell = prev_cell

        elif operations[0] == 'Z':
            restore_cell = table[deleted_stack.pop()]
            prev_cell, post_cell = table[restore_cell.before], table[restore_cell.after]
            prev_cell.after = restore_cell.myself
            post_cell.before = restore_cell.myself
            restore_cell.is_deleted = False

    del table[-1]
    answer = ''
    for key in table:
        if table[key].is_deleted:
            answer += 'X'
        else:
            answer += 'O'
    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))
