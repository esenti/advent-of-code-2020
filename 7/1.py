import re

from pathlib import Path
from collections import defaultdict
from typing import Iterable, DefaultDict, List

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [line.strip() for line in f.readlines()]


def find_bag(bags: DefaultDict[str, List[str]], outer: Iterable[str], target: str):

    for o in outer:
        if o == target:
            return True

        if o in bags and find_bag(bags, bags[o], target):
            return True

    return False


bags = defaultdict(list)

for line in lines:
    outer, inner = line.split(' bags contain ')
    inner_list = inner.split(', ')

    for i in inner_list:
        match = re.match(r'(?P<count>\d+) (?P<color>\w+ \w+)', i)
        if match:
            bags[outer].append(match.group('color'))

count = sum(find_bag(bags, bags[outer], 'shiny gold') for outer in bags if outer != 'shiny gold')

print(count)
