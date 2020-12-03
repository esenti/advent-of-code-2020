from pathlib import Path
from typing import List

import re

def count_trees(lines: List[str], dx: int, dy: int) -> int:
    x: int = 0
    y: int = 0
    t: int = 0

    while y < len(lines) - 1:
        x += dx 
        y += dy 

        val: str = lines[y][x % len(lines[y])]

        t += 1 if val == '#' else 0

    return t

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    trees: int = 1

    for dx, dy in slopes:
        trees *= count_trees(lines, dx, dy)

    print(trees)
