
class LibDynArray:

    def __init__(self) -> None:
        self.data = [None]
        self.length = 0

    def get_size(self) -> int:
        return self.length
    
    def set_value(self, ind: int, value: int) -> None:
        self.data[ind] = value

    def get_value(self, ind: int) -> int:
        return self.data[ind]
    
    def add(self, x: int) -> None:
        if len(self.data) == self.length:
            data =  [None] * (self.length * 2)
            for i in range(self.length):
                data[i] = self.data[i]  
            self.data = data 
        self.data[self.length] = x
        self.length += 1

    def remove(self):
        self.length -= 1
        if(self.length * 4 < len(self.data)):
            data = [None] * (len(self.data) // 2)
            for x in range(self.length):
                data[x] = self.data[x]
            self.data = data

    def insert(self, x: int, ind: int):
        self.add(0)
        for i in range(self.length - 1, ind, -1):
            self.data[i] = self.data[i - 1]
        self.data[ind] = x

    def print_array(self):
        print('Print array')
        for i in range(self.get_size()):
            print("Element", i, ":", self.get_value(i))