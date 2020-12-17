from pathlib import Path
from itertools import combinations

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        numbers = [int(line) for line in f.readlines()]


for i, n in enumerate(numbers[25:]):
    window = numbers[i:i + 25]

    valid = False

    for a, b in combinations(window, 2):
        if a + b == n:
            valid = True
            break

    if not valid:
        print(n)
        break
