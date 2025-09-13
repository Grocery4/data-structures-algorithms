class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.item_count = 0

        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.item_count == 0
    
    def is_full(self):
        return self.item_count >= self.size

    def first(self):
        if self.is_empty():
            print('queue is empty.')
            return
        
        return self.queue[self.head]

    def enqueue(self, value):
        if not self.is_full():
            self.queue[self.tail] = value
            self.tail = (self.tail+1) % self.size

            self.item_count += 1
        else:
            print('enqueue failed.')


    def dequeue(self):
        if self.is_empty():
            print('dequeue failed.')
            return
        
        result = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head+1) % self.size

        self.item_count -= 1

        return result