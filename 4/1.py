from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        content = f.read()

passports = content.split('\n\n')

required_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}

count = 0

for passport in passports:
    fields = passport.split()

    field_names = {v.split(':')[0] for v in fields}

    count += 1 if required_fields.issubset(field_names) else 0

print(count)