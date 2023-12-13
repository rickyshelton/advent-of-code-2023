from day_01 import parse_line, mappings, read_file


def test_mappings():
    assert mappings.get("1") == "1"
    assert mappings.get('one') == "1"

def test_example_input_1():
    assert parse_line("two1nine") == 29

def test_example_input_2():
    assert parse_line("eightwothree") == 83

def test_example_input_3():
    assert parse_line("abcone2threexyz") == 13

def test_example_input_4():
    assert parse_line("xtwone3four") == 24

def test_example_input_5():
    assert parse_line("4nineeightseven2") == 42

def test_example_input_6():
    assert parse_line("zoneight234") == 14

def test_example_input_7():
    assert parse_line("7pqrstsixteen") == 76

def test_single_word():
    assert parse_line("seven") == 77

def test_overlap():
    assert parse_line("seven7vshrlkpc2dtoneightk") == 78

def test_read_file():
    lines = read_file()
    assert len(lines) == 1000
    assert isinstance(lines, list) is True
