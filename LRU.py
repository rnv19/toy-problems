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

if __name__ == "__main__":
    q = LRU()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    q.put(6)
    print(q.get())