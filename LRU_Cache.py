from LRU import LRU

class LRUTest:

    def _init_(self):
        self.q = LRU()
        self.run()

    def run(self):
        self.q.put(1)
        print(self.check(1))
        self.q.put(2)
        print(self.check(2))
        self.q.put(3)
        print(self.check(3))
        self.q.put(4)
        print(self.check(4))
        self.q.put(5)
        print(self.check(5))

    def check(self, expected):
        queue = self.q.get_cache
        if (len(queue) == expected):
            return True
        else:
            return False

if __name__ == "__main__":
    p = LRUTest()
    p.run()