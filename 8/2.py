from pathlib import Path
from typing import Iterable, List, Tuple

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [line.strip() for line in f.readlines()]


def parse_instructions(lines: Iterable[str]) -> List[Tuple[str, int]]:
    instructions: List[Tuple[str, int]] = []

    for line in lines:
        op, arg = line.split()

        instructions.append((op, int(arg)))

    return instructions


def execute(instructions: List[Tuple[str, int]]) -> Tuple[bool, int]:
    executed_instructions = set()
    acc = 0
    ptr = 0

    while ptr not in executed_instructions:
        if ptr == len(instructions):
            return True, acc

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

    return False, acc


instructions = parse_instructions(lines)

for i, (op, arg) in enumerate(instructions):
    modified_instructions = instructions[:]

    modified_instructions[i] = ('nop', arg) if op == 'jmp' else ('jmp', arg) if op == 'nop' else (op, arg)

    terminated, acc = execute(modified_instructions)

    if terminated:
        print(acc)
        break
