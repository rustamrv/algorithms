from libs import LibArray, LibHashMap
from examples import Player

def example_array():
  arr = LibArray(10)
  myArr = arr.get_array()
  print("Init array", myArr)
  sortArray = sorted(myArr)
  print("Sort array", sortArray)
  player = Player(1600, 'Nick 3')
  arr =  [
            Player(1100, 'Nick 1'),
            Player(1200, 'Nick 2'),
            Player(1600, 'Nick 3'),
            Player(1600, 'Nick 4'),
            Player(1600, 'Nick 5'),
            Player(3000, 'Nick 6'),
            Player(4000, 'Nick 7')
        ]
  print(player.findSpot(arr))


def example_hash():
  hash_map = LibHashMap(16)
  hash_map.add("apple", "A fruit")
  hash_map.add("banana", "Yellow fruit")
  hash_map.add("apple", "A delicious fruit")
  print(hash_map.get("apple"))
  print(hash_map.get("banana"))
 
if __name__ == '__main__':
  example_hash()