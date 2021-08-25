from collections import defaultdict


class GameBoard:
    def __init__(self):
        self.size = len(game_board)
    
    def find_blanks(self, target=0):
        blanks_dict = defaultdict(list)
        visited = [[False] * self.size for _ in range(self.size)]
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for x in range(self.size):
            for y in range(self.size):
                if not visited[x][y]:
                    visited[x][y] = True
                    if game_board[x][y] == target:
                        _key = (x, y)
                        _val = [_key]
                        stack = [_key]
                        while stack:
                            curr_x, curr_y = stack.pop()
                            for dir_x, dir_y in dirs:
                                post_x, post_y = curr_x + dir_x, curr_y + dir_y
                                if 0 <= post_x < self.size and 0 <= post_y < self.size and game_board[post_x][post_y] == target and not visited[post_x][post_y]:
                                    visited[post_x][post_y] = True
                                    _val.append((post_x, post_y))
                                    stack.append((post_x, post_y))
                        blanks_dict[_key].append(_val)
        return blanks_dict
                                
        
    def filled_blanks(self):
        pass
    
class Table:
    def find_pieces(self):
        pass
    
    def rotate_piece(self):
        pass


def solution(game_board, table):
    tmp = GameBoard()
    tmp.size = len(game_board)
    print(tmp.size)
    return tmp.find_blanks()


if __name__ == "__main__":
    game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    print(solution(game_board, table))