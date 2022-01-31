# Bank card validation:
# It must only consist of exactly 16 digits (0-9)
#  It must start with a 4 ,5 or 6
#  It may have digits in groups of 4 , separated by one hyphen "-".
#  It must NOT have 4 or more consecutive repeated digits.
# valid
# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214
# invalid
# 44244x4424442444
# 0525362587961578

from itertools import groupby
import re


def consecutive_number(password: str):
    return max(len(list(g)) for _, g in groupby(password))


def valid_pattern(password: str):
    pattern = re.compile(r'(?:\d{4}-){3}\d{4}|\d{16}')
    return pattern.fullmatch(password)


def validate_password(password: str) -> bool:
    return valid_pattern(password) and consecutive_number(password.replace('-', '')) < 4


if __name__ == '__main__':
    list_of_passwords = [
        '4253625879615786',
        '4424424424442444',
        '5122-2368-7954-3214',
        '44244x4424442444',
        '0525362587961578'
    ]
    [print(f'Valid password for index {i}') for i, password in enumerate(list_of_passwords) if validate_password(password)]
