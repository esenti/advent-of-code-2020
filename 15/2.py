from pathlib import Path
from typing import Dict

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        numbers = [int(n) for n in f.read().split(',')]

past_numbers: Dict[int, int] = dict()
last_number = 0

for i in range(30000000):

    if i < len(numbers):
        current_number = numbers[i]
    else:
        if current_number not in past_numbers:
            current_number = 0
        else:
            current_number = i - past_numbers[current_number]

    past_numbers[last_number] = i
    last_number = current_number

print(last_number)
