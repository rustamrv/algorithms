from random import randint


class LibArray: 

    def __init__(self, size) -> None:
        self.__array = [randint(0, 10) for i in range(size)]


    def get_array(self):
        return self.__array

    def find_max(self):
        """
            linear search for an element in an array
        """  
        maxElement = 0
        for x in self.get_array():
            if(x > maxElement):
                maxElement = x
        print('Find max element', maxElement)

    def binary_search(self, search):  
        """
            Binary search
        """
        sortArray = sorted(self.get_array())
        left = 0
        right = len(sortArray) - 1
     
        while(left <= right): 
            middle = (left + right) // 2 
            if(sortArray[middle] < search):  
                left = middle + 1
            elif (sortArray[middle] > search):
                right = middle - 1 
            else:
                return middle
        return -1