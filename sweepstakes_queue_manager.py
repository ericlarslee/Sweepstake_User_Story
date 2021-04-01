from queue_data import Queue


class QueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, entry):
        self.queue.enqueue(entry)

    def get_sweepstakes(self):
        self.queue.dequeue()