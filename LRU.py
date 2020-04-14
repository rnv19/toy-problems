from queue import Queue

class LRU:
    def __init__(self, size):
        # initialize a queue when LRU is called
        self.queue = Queue(maxsize = 5)
        