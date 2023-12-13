from day_01 import parse_line, get_first_number, get_last_number, read_file


def test_example_input_1():
    assert parse_line("1abc2") == 12

def test_example_input_2():
    assert parse_line("pqr3stu8vwx") == 38

def test_example_input_3():
    assert parse_line("a1b2c3d4e5f") == 15

def test_example_input_4():
    assert parse_line("treb7uchet") == 77

def test_get_first_number():
    assert get_first_number('1a2') == '1'

def test_get_last_number():
    assert get_last_number('1a2') == '2'

def test_get_last_number2():
    assert get_last_number('1a23') == '3'

def test_read_file():
    lines = read_file()
    assert len(lines) == 1000
    assert isinstance(lines, list) is True
