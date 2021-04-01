from contestant import Contestant
import random


class Sweepstake:
    def __init__(self, name):
        self.contestants = {}
        self.name = name
        self.registration_number = 0

    def register_contestant(self):
        fname_entry = input('What is the contestant\'s first name?\n')
        lname_entry = input('What is the contestant\'s last name?\n')
        email_entry = input('What is the contestant\'s email address?')
        self.registration_number += 1
        temp_person = (Contestant(fname_entry, lname_entry, email_entry, self.registration_number))
        self.contestants[temp_person.registration_number] = {temp_person}

    def pick_winner(self):
        winner_temp = random.choice(list(self.contestants.items()))
        return winner_temp

    def print_contestant_info(self):
        pass
