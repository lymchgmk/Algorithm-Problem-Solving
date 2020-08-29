arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(arr1)):
    for j in range(len(arr1)):
        if i < j:
            arr1[i][j], arr1[j][i] = arr1[j][i], arr1[i][j]

print(arr1)



arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(arr2)):
    for j in range(i+1, len(arr2[i])):
            arr2[i][j], arr2[j][i] = arr2[j][i], arr2[i][j]

print(arr2)