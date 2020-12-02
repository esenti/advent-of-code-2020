from pathlib import Path

import re

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

pattern = r'(?P<min>\d+)-(?P<max>\d+) (?P<char>[a-z]): (?P<val>.*)'

c: int = 0

for line in lines:
    m = re.match(pattern, line)

    c += int(m is not None and (m.group('val')[int(m.group('min')) - 1] == (m.group('char'))) != (m.group('val')[int(m.group('max')) - 1] == (m.group('char'))))

print(c)