from queue import Queue
from collections import deque

class LRU:
    def __init__(self):
        # initialize a queue when LRU is called
        # q = Queue.Queue(maxsize=0)
        # self.queue = Queue(maxsize=0)
        self.queue = deque(maxlen = 5)
    
    def put(self, item):
        # self.queue.append(item)
        self.queue.append(item)

    def get(self):
        return self.queue.popleft()

    def get_cache(self):
        return self.queue