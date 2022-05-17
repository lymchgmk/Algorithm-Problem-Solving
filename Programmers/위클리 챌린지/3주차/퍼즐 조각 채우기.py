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
        def _make_rotated_pieces(piece):
            rotated_pieces = [piece]
            for _ in range(3):
                piece = list(zip(*piece[::-1]))
                rotated_pieces.append([list(p) for p in piece])
            return rotated_pieces
        
        def _check(blank, rotated_pieces):
            for rotated_piece in rotated_pieces:
                if blank == rotated_piece:
                    return True
            else:
                return False
    
        # align
        blank_xs, blank_ys = [x for x, y in blank], [y for x, y in blank]
        piece_xs, piece_ys = [x for x, y in piece], [y for x, y in piece]
        
        blank_min_x, blank_max_x, blank_min_y, blank_max_y = min(blank_xs), max(blank_xs), min(blank_ys), max(blank_ys)
        piece_min_x, piece_max_x, piece_min_y, piece_max_y = min(piece_xs), max(piece_xs), min(piece_ys), max(piece_ys)
        
        aligned_blank = [[0] * (blank_max_y - blank_min_y + 1) for _ in range(blank_max_x - blank_min_x + 1)]
        aligned_piece = [[0] * (piece_max_y - piece_min_y + 1) for _ in range(piece_max_x - piece_min_x + 1)]
        for x, y in blank:
            aligned_blank[x-blank_min_x][y-blank_min_y] = 1
        for x, y in piece:
            aligned_piece[x-piece_min_x][y-piece_min_y] = 1
        
        # _check
        return _check(aligned_blank, _make_rotated_pieces(aligned_piece))

    blanks_dict = find_pieces(game_board, 0)
    pieces_dict = find_pieces(table, 1)
    
    answer = 0
    for size in range(1, 7):
        blanks, pieces = blanks_dict[size], pieces_dict[size]
        for blank in blanks:
            tmp_pieces = []
            while pieces:
                piece = pieces.pop()
                if rotate_check(blank, piece):
                    answer += size
                    break
                tmp_pieces.append(piece)
            pieces = pieces + tmp_pieces
    return answer


'''
from collections import Counter
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def neighbors(self):
        return [
            Pos(self.x, self.y - 1),
            Pos(self.x + 1, self.y),
            Pos(self.x, self.y + 1),
            Pos(self.x - 1, self.y),
        ]


def make_tile_from_positions(positions):
    """Smallest possible representation with rotation"""

    def rotate90(tile):
        return tuple(
            tuple(tile[i][j] for i in range(len(tile)))
            for j in reversed(range(len(tile[0])))
        )

    positions = set(positions)

    xs = [pos.x for pos in positions]
    min_x = min(xs)
    max_x = max(xs)

    ys = [pos.y for pos in positions]
    min_y = min(ys)
    max_y = max(ys)

    tile_representations = [
        tuple(
            tuple(Pos(i, j) in positions for j in range(min_y, max_y + 1))
            for i in range(min_x, max_x + 1)
        )
    ]

    for __ in range(3):
        tile_representations.append(rotate90(tile_representations[-1]))

    return min(tile_representations)


def get_tile_size(tile):
    return sum(sum(row) for row in tile)


def parse_tiles(board, tile_value=1):
    n = len(board)

    # Add sentinel boundaries
    sentinel = 1 - tile_value

    board = [
        [sentinel] * (n + 2),
        *([sentinel] + row + [sentinel] for row in board),
        [sentinel] * (n + 2),
    ]

    # Detect tiles
    tile_positions = []
    for i, j in product(range(1, n + 1), range(1, n + 1)):
        if board[i][j] == tile_value:
            stack = [Pos(i, j)]
            squares = []
            while stack:
                curr = stack.pop()
                board[curr.x][curr.y] = sentinel
                squares.append(curr)
                for neighbor in curr.neighbors():
                    if board[neighbor.x][neighbor.y] == tile_value:
                        stack.append(neighbor)
            tile_positions.append(squares)

    # Make tiles
    tiles = [make_tile_from_positions(p) for p in tile_positions]

    return tiles


def solution(game_board, table):
    tiles = parse_tiles(table, 1)
    empty_spaces = parse_tiles(game_board, 0)

    tile_counter = Counter(tiles)
    empty_space_counter = Counter(empty_spaces)

    used_tiles = tile_counter & empty_space_counter

    return sum(get_tile_size(tile) * occ for tile, occ in used_tiles.items())
'''


if __name__ == "__main__":
    game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    print(solution(game_board, table))
    