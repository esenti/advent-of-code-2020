from pathlib import Path
from itertools import chain

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        content = f.read()

groups = content.split('\n\n')

count = 0

for group in groups:
    votes = group.split()
    votes_set = set(chain.from_iterable(votes))
    count += len(votes_set)

print(count)