from day_02 import get_game_power

def test_get_game_power():
    assert get_game_power({'red':2, 'green':3, 'blue':4}) == 24
    assert get_game_power({'red':1, 'green':1, 'blue':1}) == 1
