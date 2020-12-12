import re

from pathlib import Path
from collections import defaultdict
from typing import Iterable, DefaultDict, List, Tuple

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [line.strip() for line in f.readlines()]


def count_bags(bags: DefaultDict[str, List[Tuple[str, int]]], outer: Iterable[Tuple[str, int]]):

    total_count = 0

    for color, count in outer:
        total_count += count
        if color in bags:
            total_count += count * count_bags(bags, bags[color])

    return total_count


bags = defaultdict(list)

for line in lines:
    outer, inner = line.split(' bags contain ')
    inner_list = inner.split(', ')

    for i in inner_list:
        match = re.match(r'(?P<count>\d+) (?P<color>\w+ \w+)', i)
        if match:
            bags[outer].append((match.group('color'), int(match.group('count'))))

print(count_bags(bags, bags['shiny gold']))
