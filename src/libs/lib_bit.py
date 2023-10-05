

class Bitset:

    def __init__(self, n: int) -> None:
        self.data = [0] * (n // 32 + 1)

    def get(self, ind: int):
        x = self.data[ind // 32]
        return (x >> (ind % 32)) & 1
    
    def set_value(self, ind: int, value: int):
        if self.get(ind) == value:
            return
        self.data[ind // 32] ^= 1 << (ind % 32)