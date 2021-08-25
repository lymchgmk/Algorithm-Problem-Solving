from collections import defaultdict


def solution(game_board, table):
    def find_pieces(_board, target):
        pieces_dict = {}
        N = len(_board)
        visited = [[False] * N for _ in range(N)]
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for x in range(N):
            for y in range(N):
                if not visited[x][y]:
                    visited[x][y] = True
                    if _board[x][y] == target:
                        _key = (x, y)
                        _val = [_key]
                        stack = [_key]
                        while stack:
                            curr_x, curr_y = stack.pop()
                            for dir_x, dir_y in dirs:
                                post_x, post_y = curr_x + dir_x, curr_y + dir_y
                                if 0 <= post_x < N and 0 <= post_y < N and _board[post_x][post_y] == target and not visited[post_x][post_y]:
                                    visited[post_x][post_y] = True
                                    _val.append((post_x, post_y))
                                    stack.append((post_x, post_y))
                        pieces_dict[_key] = _val
        
        result_dict = defaultdict(list)
        for val in pieces_dict.values():
            result_dict[len(val)].append(val)
        return result_dict
    
    # 어떻게 해야 blank-piece의 모양이 같음을 알 수 있을까?
    def rotate_piece():
        pass
    
    blanks = find_pieces(game_board, 0)
    pieces = find_pieces(table, 1)
    
    for blank_size in blanks:
        print(blank_size)
    

if __name__ == "__main__":
    game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    print(solution(game_board, table))