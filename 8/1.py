from pathlib import Path
from typing import Sequence, Iterable, List, Tuple

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [line.strip() for line in f.readlines()]


def parse_instructions(lines: Iterable[str]) -> Sequence[Tuple[str, int]]:
    instructions: List[Tuple[str, int]] = []

    for line in lines:
        op, arg = line.split()

        instructions.append((op, int(arg)))

    return instructions


instructions = parse_instructions(lines)
executed_instructions = set()
acc = 0
ptr = 0


while ptr not in executed_instructions:
    executed_instructions.add(ptr)

    op: str
    arg: int
    op, arg = instructions[ptr]

    if op == 'acc':
        acc += arg
        ptr += 1
    elif op == 'jmp':
        ptr += arg
    else:
        ptr += 1

print(acc)
