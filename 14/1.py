from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [line.strip() for line in f.readlines()]


class Mem(dict):

    def __init__(self):
        self.mask1 = 0
        self.mask0 = 1
        super().__init__()

    def __setitem__(self, k, v):
        super().__setitem__(k, v & self.mask1 | self.mask0)


mem = Mem()

for line in lines:
    lhs, rhs = line.split(' = ')
    if lhs == 'mask':
        mem.mask1 = eval('0b' + rhs.replace('X', '1'))
        mem.mask0 = eval('0b' + rhs.replace('X', '0'))
    else:
        exec(line)

print(sum(mem.values()))
