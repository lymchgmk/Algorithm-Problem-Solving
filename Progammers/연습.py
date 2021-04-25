board = [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]
for i, j in zip(range(len(board)), range(len(board) - 1, -1, -1)):
    print(board[i][j])

print()

for i, j in zip(range(len(board)), range(len(board))):
    print(board[i][j])