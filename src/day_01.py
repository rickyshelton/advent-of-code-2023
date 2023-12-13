import re
import sys

def parse_line(line: str) -> int:
    first = get_first_number(line)
    last = get_last_number(line)

    return int(first + last)

def get_first_number(line: str) -> str:
    return re.search('\\d', line).group()

def get_last_number(line: str) -> str:
    return re.findall('\\d', line)[-1]

def read_file() -> list:
    with open("src/day_01_input.txt", "r") as file:
        return file.readlines()

def get_calibration_values_total():
    lines = read_file()
    total = 0

    for line in lines:
        total += parse_line(line)
        print(total)

    print(total)
    return 0

if __name__ == '__main__':
    sys.exit(get_calibration_values_total())
