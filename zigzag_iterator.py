from collections import deque

class ZigzagIterator:
    def __init__(self, v1, v2):
        self.queue = deque()

        if v1:
            self.queue.append(iter(v1))
        if v2:
            self.queue.append(iter(v2))

    def next(self):
        iterator = self.queue.popleft()
        value = next(iterator)

        try:
            next_value = next(iterator)
            self.queue.append(iter([next_value] + list(iterator)))
        except StopIteration:
            pass

        return value

    def hasNext(self):
        return len(self.queue) > 0
