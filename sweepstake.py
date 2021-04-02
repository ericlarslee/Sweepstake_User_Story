from contestant import Contestant
import random


def continue_prompt(text):
    switcher = {
        "y": True,
        "yes": True,
        "Yes": True
    }
    user_input = input(text).lower()
    return switcher.get(user_input, False)


class Sweepstake:
    def __init__(self):
        self.contestants = {}
        self.name = input('Please input a name for this sweepstakes')
        self.registration_number = 0
        self.populate_contestant_dict()

    def register_contestant(self):
        fname_entry = input('What is the contestant\'s first name?\n')
        lname_entry = input('What is the contestant\'s last name?\n')
        email_entry = input('What is the contestant\'s email address?')
        self.registration_number += 1
        temp_person = (Contestant(fname_entry, lname_entry, email_entry, self.registration_number))
        self.contestants[temp_person.registration_number] = {temp_person}

    def populate_contestant_dict(self):
        will_proceed = True
        while will_proceed:
            response = continue_prompt('Are there contestants to be registered?')
            if response:
                self.register_contestant()
                return True
            else:
                return False

    def pick_winner(self):
        winner_temp = random.choice(list(self.contestants.items()))
        return winner_temp

    def print_contestant_info(self):
        for contestant in self.contestants:
            print(f'{contestant.first_name} {contestant.last_name}, {contestant.email_address}, {contestant.registration_number}')
