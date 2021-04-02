import os


def simulation_main_menu():
    """Main menu prompting user to choose an option"""
    validate_user_selection = (False, None)
    while validate_user_selection[0] is False:
        print("\t\t-Simulation menu-")
        print("\tPress -1- to generate a new sweepstakes")
        print("\tPress -2- to add sweepstake to data list")
        print("\tPress -3- to remove sweepstake from data list")
        print("\tPress -4- to terminate simulation")
        user_input = try_parse_int(input())
        validate_user_selection = validate_main_menu(user_input)
    return validate_user_selection[1]


def validate_main_menu(user_input):
    """Validation function that checks if 'user_input' argument is an int 1-4. No errors."""
    switcher = {
        1: (True, 1),
        2: (True, 2),
        3: (True, 3),
        4: (True, 4),
    }
    return switcher.get(user_input, (False, None))


def try_parse_int(value):
    """Attempts to parse a string into an integer, returns 0 if unable to parse. No errors."""
    try:
        return int(value)
    except:
        return 0