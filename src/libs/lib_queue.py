

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

# class LibQueue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.empty():
#             return self.items.pop(0)
#         else:
#             print("Очередь пуста")

#     def empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

#     def peek(self):
#         if not self.empty():
#             return self.items[0]
#         else:
#             print("Очередь пуста")

#     def clear(self):
#         self.items = []

#     def front(self):
#         return self.peek()

#     def back(self):
#         if not self.empty():
#             return self.items[-1]
#         else:
#             print("Очередь пуста")
