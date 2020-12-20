from pathlib import Path
from typing import List

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [line.strip() for line in f.readlines()]


class Mem(dict):

    def __init__(self):
        self.floating = []
        self.mask0 = 1
        super().__init__()

    def __setitem__(self, k, v):
        k = k | self.mask0
        addresses = [k]

        for f in self.floating:
            self.generate_addresses(f, addresses)

        for address in addresses:
            super().__setitem__(address, v)

    def generate_addresses(self, i: int, a: List[int]):
        for x in range(len(a)):
            a[x] = a[x] | (1 << i)
            a.append(a[x] & ~(1 << i))


mem = Mem()

for line in lines:
    lhs, rhs = line.split(' = ')
    if lhs == 'mask':
        mem.floating = [35 - i for i, x in enumerate(rhs) if x == 'X']
        mem.mask0 = eval('0b' + rhs.replace('X', '0'))
    else:
        exec(line)

print(sum(mem.values()))
