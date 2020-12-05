from pathlib import Path

import re

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        content = f.read()

passports = content.split('\n\n')

def validate_int_range(v: str, vmin: int, vmax: int) -> bool:
    try:
        vi = int(v)
        return vmin <= vi <= vmax
    except: 
        return False

def validate_height(v: str) -> bool:
    match = re.match(r'^(\d+)(\D+)$', v)

    limits = {
        'cm': (150, 193),
        'in': (59, 76),
    }

    if not match:
        return False

    return limits[match.group(2)][0] <= int(match.group(1)) <= limits[match.group(2)][1]

field_validators = {
    'byr': lambda v: validate_int_range(v, 1920, 2002),
    'iyr': lambda v: validate_int_range(v, 2010, 2020),
    'eyr': lambda v: validate_int_range(v, 2020, 2030),
    'hgt': lambda v: validate_height(v),
    'hcl': lambda v: re.match(r'^#[0-9a-f]{6}$', v) is not None,
    'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda v: re.match(r'^[0-9]{9}$', v) is not None,
}

count = 0

for passport in passports:
    fields = passport.split()
    required_fields = set(field_validators.keys())
    valid = True

    for field in fields:
        k, v = field.split(':')

        if k in field_validators and not field_validators[k](v):
            valid = False
            break

        if k in required_fields:
            required_fields.remove(k)

    count += 1 if valid and len(required_fields) == 0 else 0

print(count)