from collections import defaultdict


def solution(game_board, table):
    def find_pieces(_board, target):
        pieces_dict = {}
        N = len(_board)
        visited = [[False]*N for _ in range(N)]
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
        
    def rotate_check(blank, piece):
        def _rotate_90(array):
            return list(zip(*array[::-1]))
    
        # align
        blank_xs, blank_ys = [x for x, y in blank], [y for x, y in blank]
        piece_xs, piece_ys = [x for x, y in piece], [y for x, y in piece]
        
        blank_min_x, blank_max_x, blank_min_y, blank_max_y = min(blank_xs), max(blank_xs), min(blank_ys), max(blank_ys)
        piece_min_x, piece_max_x, piece_min_y, piece_max_y = min(piece_xs), max(piece_xs), min(piece_ys), max(piece_ys)
        
        aligned_blank = [[0]*(blank_max_y - blank_min_y + 1) for _ in range(blank_max_x - blank_min_x + 1)]
        for x, y in blank:
            aligned_blank[x-blank_min_x][y-blank_min_y] = 1
        for x in range(blank_max_x - blank_min_x + 1):
            aligned_blank[x] = tuple(aligned_blank[x])
            
        aligned_piece = [[0]*(piece_max_y - piece_min_y + 1) for _ in range(piece_max_x - piece_min_x + 1)]
        for x, y in piece:
            aligned_piece[x-piece_min_x][y-piece_max_y] = 1
        
        # 회전 및 비교
        # blank는 그냥 두고 piece를 회전하자
        _check = False
        for _ in range(4):
            if aligned_piece != aligned_blank:
                aligned_piece = _rotate_90(aligned_piece)
        else:
            _check = True
        return _check


    blanks_dict = find_pieces(game_board, 0)
    pieces_dict = find_pieces(table, 1)

    print(f'blanks: {blanks_dict}')
    print(f'pieces: {pieces_dict}')
    
    answer = 0
    for size in range(1, 7):
        if size <= 2 and blanks_dict[size]:
            answer += size * min(len(blanks_dict[size]), len(pieces_dict[size]))
        else:
            if
    
    return answer
    

if __name__ == "__main__":
    game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    print(solution(game_board, table))
    