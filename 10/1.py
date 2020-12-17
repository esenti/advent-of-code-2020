from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        adapters = [int(line) for line in f.readlines()]


adapters.sort()
adapters = [0] + adapters + [adapters[-1] + 3]

differences = {
    1: 0,
    2: 0,
    3: 0
}

for a, b in zip(adapters, adapters[1:]):
    differences[b - a] += 1

print(differences[1] * differences[3])
