from day_02 import get_game_id, get_sets, get_colour_totals, is_set_possible

def test_get_game_id():
    assert get_game_id('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == '1'
    assert get_game_id('Game 2: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == '2'
    assert get_game_id('Game 10: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == '10'

def test_get_sets():
    sets = get_sets('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    print(sets)
    assert len(sets) == 3
    assert sets[0] == '3 blue, 4 red'
    assert sets[1] == '1 red, 2 green, 6 blue'
    assert sets[2] == '2 green'

def test_get_colour_totals():
    assert(get_colour_totals('4 blue, 3 red')) == {'blue': 4, 'red': 3}
    assert(get_colour_totals('4 blue, 3 red, 7 green')) == {'blue': 4, 'red': 3, 'green': 7}
    assert(get_colour_totals('4 blue, 3 red, 7 green, 1 green')) == {'blue': 4, 'red': 3, 'green': 8}

def test_is_set_possible():
    assert(is_set_possible({'blue': 4, 'red': 3, 'green': 7}) is True)
    assert(is_set_possible({'blue': 4, 'red': 13, 'green': 7}) is False)
