import re
import sys

MAXIMUMS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def get_game_id(game_line: str) -> str:
    game_id_regex = r'(?<=Game )\d+(?:)'
    return re.search(game_id_regex, game_line).group()

def get_sets(game: str) -> list[str]:
    return game.split(': ')[1].split('; ')

def get_colour_totals(game_set: list[str]) -> dict[str, int]:
    colour_totals = {}

    colour_counts = game_set.split(', ')

    for colour_count in colour_counts:
        count_and_colour = colour_count.split()
        count = int(count_and_colour[0])
        colour = count_and_colour[1]

        if colour in colour_totals:
            colour_totals[colour] += count
        else:
            colour_totals[colour] = count

    return colour_totals

def is_set_possible(colour_totals: dict[str, int]) -> bool:

    for colour in colour_totals.keys():
        if colour_totals.get(colour) > MAXIMUMS.get(colour):
            return False

    return True

def get_game_lines() -> list[str]:
    with open("src/day_02_input.txt", "r") as file:
        return file.readlines()

def get_game_power(game_minimums: dict[str, int]) -> int:
    power = 1

    for colour in game_minimums.keys():
        power = power * game_minimums.get(colour)

    return power


def main():
    possible_game_id_totals = 0
    power_totals = 0
    games = get_game_lines()

    for game in games:
        game_id = int(get_game_id(game))
        game_possible = True
        game_sets = get_sets(game)
        game_minimums = {}

        for game_set in game_sets:
            colour_totals = get_colour_totals(game_set)

            for colour in colour_totals.keys():
                colour_count = colour_totals.get(colour)

                if colour in game_minimums:
                    if colour_count > game_minimums.get(colour):
                        game_minimums[colour] = colour_count
                else:
                    game_minimums[colour] = colour_count

            if not is_set_possible(colour_totals):
                game_possible = False

        if game_possible:
            possible_game_id_totals += game_id

        power = get_game_power(game_minimums)
        power_totals = power_totals + power


    print(f'Possible game totals {possible_game_id_totals}')
    print(f'Power totals {power_totals}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
