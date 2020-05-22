def issafe(arr, node):
    if 0 <= node[0] < len(arr) and 0 <= node[1] < len(arr) and arr[node[0]][node[1]]==0:
        return True
    return False


def dfs(arr, start, end):
    global visited
    stack = []
    stack.append(start)
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while stack:
        temp = stack.pop()

        if temp == end:
            return

        for dir in dirs:
            test = [temp[0] + dir[0], temp[1] + dir[1]]
            if issafe(arr, test) and test not in visited:
                visited.append(test)
                dfs(arr, test, end)

arr=[[0,0,0],[0,0,0],[0,0,0]]
visited=[]
visited.append([0,0])
dfs(arr, [0,0], [2,2])
print(visited)