

class LibSort:

    def __init__(self, data: list) -> None:
        self.data = data
    
    def bubble_sort(self):
        # O(n2)
        f: bool = True
        for j in range(0, len(self.data)):
            f = False
            for i in range(0, len(self.data) - 1 - j):
                if(self.data[i] > self.data[i + 1]):
                    self.data[i],  self.data[i + 1] =  self.data[i + 1],  self.data[i]
                    f = True
            if not f:
                break
    
    def select_sort(self):
        # O(n2)
        for i in range(0, len(self.data)):
            min_index = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i],  self.data[min_index] =  self.data[min_index],  self.data[i]

    def insert_into_sorted(self, x: int):
        pt = len(self.data)
        for i in range(0, len(self.data)):
            if(self.data[i] > x):
                pt = i
                break

        self.data.append(0)
        for i in range(len(self.data) - 1, pt, -1):
            self.data[i] = self.data[i - 1]

        self.data[pt] = x

    def insert_sort(self):
        # O(n2)
        for i in range(0, len(self.data)):
            c = self.data[i]
            pt = i
            while pt > 0 and self.data[pt - 1] > c:
                self.data[pt] = self.data[pt - 1]
                pt -= 1
            self.data[pt] = c
        
    def counter_sort(self):
        data_cnt = [0] * 1000
        for i in range(0, len(self.data)):
            data_cnt[self.data[i]] += 1
        pt = 0
        for i in range(0, len(data_cnt)):
            for j in range(0, data_cnt[i]):
                self.data[pt] = i
                pt += 1
            
