from stack_data import Stack


class StackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, entry):
        self.stack.push(entry)

    def get_sweepstakes(self):
        return self.stack.pop
