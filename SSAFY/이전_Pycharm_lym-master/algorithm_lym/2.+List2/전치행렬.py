#i : 행의 좌표, len(arr)
#j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6], [7,8,9]] # 3*3행렬
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)

#------------------------------------------------

arr = [[1,2,3],[4,5,6], [7,8,9]] # 3*3행렬
for i in range(len(arr)):
    for j in range(i+1, len(arr[i])):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)