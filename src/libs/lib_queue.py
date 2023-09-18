

class LibQueue:

    def __init__(self, max_size) -> None:
        self.data = [None] * max_size
        self.head = 0
        self.tail = 0
    
    def empty(self) -> bool:
        return self.head == self.tail
    
    def enqueue(self, x: int):
        if (self.tail + 1 == self.head or (self.tail + 1 == len(self.data) and self.head == 0)):
            print('No more size in queue')
            return
        self.data[self.tail] = x
        self.tail += 1
        if(self.tail >= len(self.data)):
            self.tail = 0
        
    def dequeue(self):
        if (self.empty()):
            print('Popping from empty queue')
            return
        t = self.data[self.head]
        self.data[self.head] = 0
        self.head += 1
        if(self.head >= len(self.data)):
            self.head = 0
        return t
    
    def peek(self) -> int:
        if self.empty():
            print('Peeking into an empty queue')
            return None 
        return self.data[self.head]