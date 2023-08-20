from typing import List, Optional

class Entry:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class LibHashMap:

    def __init__(self, size: int) -> None:
        self.entries = [None] * size
        self.size = size
        self.number_of_elements = 0

    def hash_func(self, key: str) -> int:
        return hash(key) % self.size
    
    def resize(self, size: int) -> None:
        # create new array
        new_entries = [None] * size
        # copy element from old array
        for entry in self.entries:
            index = self.find_good_index(entry.key)
            new_entries[index] = entry
        self.entries = new_entries
        self.size = size

    
    def add(self, key: str, value: str):
        index = self.find_good_index(key)
        self.entries[index] = Entry(key, value)
        self.number_of_elements += 1
        if self.number_of_elements == self.size:
            self.resize(self.size * 2)

    def get(self, key: str) -> Optional[str]:
        index = self.find_good_index(key)
        if index == -1:
            return None
        entry = self.entries[index]
        if entry is None: 
            return None
        return entry.value
    
    def find_good_index(self, key: str) -> int:  
        hash = self.hash_func(key)
        index = hash % self.size
        for i in range(self.size):
           probing_index = (index + i) % self.size
           entry = self.entries[probing_index]
           if entry is None or entry.key == key:
               return probing_index

        return -1


