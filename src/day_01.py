import re
import sys

mappings = {
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

REGEX = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

def parse_line(line: str) -> int:
    first, last = get_first_last_number(line)
    return int(first + last)

def get_first_last_number(line: str) -> (str, str):
    matches = re.findall(REGEX, line)
    return mappings.get(matches[0]), mappings.get(matches[-1])

def read_file() -> list:
    with open("src/day_01_input.txt", "r") as file:
        return file.readlines()

def get_calibration_values_total():
    lines = read_file()
    total = 0

    for line in lines:
        total += parse_line(line)

    print(f"total = {total}")
    return 0

if __name__ == '__main__':
    sys.exit(get_calibration_values_total())
