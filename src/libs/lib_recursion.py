

class LibRecursion:

    def __init__(self, data) -> None:
        self.data = data

    def gen(self, x: int, n: int):
        if x == n:
            return
        letters = list('abcdefghijklmnopqrstuvwxyz')
        for self.data[x] in letters:
            if x > 0 and self.data[x] == self.data[x - 1]:
                continue
            self.gen(x + 1, n)
