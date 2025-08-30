class Stack:
    def __init__(self, size):
        self.stack = [None for _ in range(size)]
        self.last_position = -1

    def is_empty(self):
        for elem in self.stack:
            if elem != None:
                return False
        return True
    
    def push(self,value):
        for i in range(len(self.stack)):
            if self.stack[i] == None:
                self.stack[i] = value
                self.last_position = i
                return
        
    def pop(self):
        if self.last_position != -1:
            result = self.stack[self.last_position]
            self.stack[self.last_position] = None
            self.last_position -= 1
            return result

    def top(self):
        return self.stack[self.last_position]

    def is_full(self):
        if self.last_position == len(self.stack)-1:
            return True
        return False