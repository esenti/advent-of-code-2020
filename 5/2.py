from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

def binary_search(v: str, i: int, l: int, h: int, lc: str, hc: str) -> int:
    r = round((h - l) / 2)

    if (r == 0):
        return l if v[i] == lc else h

    if (v[i]) == lc:
        return binary_search(v, i + 1, l, h - r, lc, hc)
    elif (v[i] == hc):
        return binary_search(v, i + 1, l + r, h, lc, hc)
    else:
        return -1

ids = []

for line in lines:
    row = binary_search(line, 0, 0, 127, 'F', 'B')
    column = binary_search(line, 7, 0, 7, 'L', 'R')

    seat_id = row * 8 + column
    ids.append(seat_id)

ids.sort()

for a, b in zip(ids, ids[1:]):
    if a + 1 != b:
        print(a + 1)
