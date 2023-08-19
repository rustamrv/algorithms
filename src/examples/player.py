from __future__ import annotations

from typing import TypeVar

T = TypeVar('T', bound='Player')

class Player:

    def __init__(self, rating, nickName) -> None:
        self.rating = rating
        self.nickName = nickName


    def findSpot(self, arr: [T]):
        """
        Find element using binary search   
        """
        left = 0
        right = len(arr) - 1
     
        while(left < right): 
            middle = (left + right) // 2 
            if(arr[middle].rating < self.rating):  
                left = middle + 1
            else:
                right = middle 
                 
        return left