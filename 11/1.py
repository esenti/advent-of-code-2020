from pathlib import Path
from itertools import product
from typing import List, Tuple

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        board = [list(line.strip()) for line in f.readlines()]


def check_position(board: List[List[str]], x: int, y: int) -> int:
    if x < 0 or y < 0:
        return 0

    if y >= len(board) or x >= len(board[y]):
        return 0

    return 1 if board[y][x] == '#' else 0


def count_neighbours(board: List[List[str]], x: int, y: int) -> int:
    count = 0
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        if not (dx == 0 and dy == 0):
            count += check_position(board, x + dx, y + dy)

    return count


def simulate(board: List[List[str]]) -> Tuple[List[List[str]], bool]:
    result = [['x'] * len(r) for r in board]
    changed = False

    for y, row in enumerate(board):
        for x, v in enumerate(row):
            if v == 'L' and count_neighbours(board, x, y) == 0:
                result[y][x] = '#'
                changed = True
            elif v == '#' and count_neighbours(board, x, y) >= 4:
                result[y][x] = 'L'
                changed = True
            else:
                result[y][x] = v

    return result, changed


changed = True

while changed:
    board, changed = simulate(board)

occupied = sum(sum([1 for v in row if v == '#']) for row in board)
print(occupied)
