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
dx = 10
dy = 1

for i, arg in instructions:

    if i == 'N':
        dy += arg
    elif i == 'E':
        dx += arg
    elif i == 'S':
        dy -= arg
    elif i == 'W':
        dx -= arg
    elif i == 'F':
        x += arg * dx
        y += arg * dy
    elif i == 'R':
        dx, dy = rotate(dx, dy, arg)
    elif i == 'L':
        dx, dy = rotate(dx, dy, -arg)

print(abs(x) + abs(y))
