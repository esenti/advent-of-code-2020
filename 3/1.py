from pathlib import Path

import re

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [l.strip() for l in f.readlines()]

x: int = 0
y: int = 0
t: int = 0

while y < len(lines) - 1:
    x += 3
    y += 1

    val: str = lines[y][x % len(lines[y])]

    t += 1 if val == '#' else 0

print(t)