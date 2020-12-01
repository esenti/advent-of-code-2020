from pathlib import Path
from itertools import combinations

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

    numbers = (int(l) for l in lines)

    for a, b in combinations(numbers, 2):
        if a + b == 2020:
            print(a * b)
            break