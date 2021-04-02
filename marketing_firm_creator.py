from sweepstakes_queue_manager import QueueManager
from sweepstakes_stack__manager import StackManager


class MarketingFirmCreator:
    def __init__(self):
        self.manager_selection()

    def manager_selection(self):
        while True:
            selection = input('Do you want your sweepstakes to be managed with a stack or queue?')
            if selection == 'stack':
                return False, StackManager()
            elif selection == 'queue':
                return False, QueueManager()
            else:
                print('That is not a valid entry')

