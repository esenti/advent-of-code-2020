from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

earliest_departure = int(lines[0])
buses = [int(i) for i in lines[1].split(',') if i != 'x']

run = True
departure = earliest_departure
earliest_bus = None

while run:
    departure += 1

    for bus in buses:
        if departure % bus == 0:
            earliest_bus = bus
            run = False
            break

print(bus * (departure - earliest_departure))
