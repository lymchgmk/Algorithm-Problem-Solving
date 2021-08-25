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
        
        tmp = {}
        for key, values in result_dict.items():
            tmp[key] = []
            for value in values:
                center_x, center_y = 0, 0
                _set = set()
                for x, y in value:
                    center_x += x
                    center_y += y
                center_x /= len(value)
                center_y /= len(value)
                
                for x, y in value:
                    _set.add((x - center_x, y - center_y))
            tmp[key].append(_set)
        
        print(tmp)
        print()
        
        # 1. 무게 중심 구하기
        
        # 2. 각 원소애서 무게 중심 값을 빼기
        
        # 3. 교체
        return result_dict
    
    # 어떻게 해야 blank-piece의 모양이 같음을 알 수 있을까?
    # 무게 중심이랑 각 블럭들 간의 차이를 가지고 set으로 표현하면 되나?
    # 최소 1개에서 최대 6개까지 연결된 퍼즐 조각
    def rotate_piece():
        pass
    
    blanks = find_pieces(game_board, 0)
    pieces = find_pieces(table, 1)
    

if __name__ == "__main__":
    game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    print(solution(game_board, table))