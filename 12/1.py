from pathlib import Path
from typing import Tuple

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        instructions = [(line[0], int(line[1:])) for line in f.readlines()]


def rotate(x: int, y: int, arg: int) -> Tuple[int, int]:
    rx = x
    ry = y
    s = 1 if arg >= 0 else -1

    for _ in range(abs(arg) // 90):
        rx, ry = (s * ry, -s * rx)

    return rx, ry


x = 0
y = 0
dx = 1
dy = 0

for i, arg in instructions:

    if i == 'N':
        y += arg
    elif i == 'E':
        x += arg
    elif i == 'S':
        y -= arg
    elif i == 'W':
        x -= arg
    elif i == 'F':
        x += arg * dx
        y += arg * dy
    elif i == 'R':
        dx, dy = rotate(dx, dy, arg)
    elif i == 'L':
        dx, dy = rotate(dx, dy, -arg)

print(abs(x) + abs(y))
