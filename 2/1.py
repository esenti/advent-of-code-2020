from pathlib import Path

import re

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

pattern = r'(?P<min>\d+)-(?P<max>\d+) (?P<char>[a-z]): (?P<val>.*)'

c: int = 0

for line in lines:
    m = re.match(pattern, line)

    c += int(m is not None and int(m.group('min')) <= m.group('val').count(m.group('char')) <= int(m.group('max')))

print(c)