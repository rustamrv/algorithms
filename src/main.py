from libs import LibArray, LibHashMap, LibDynArray, LinkedList, DLinkedList
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

def example_dyn_arr(): 
  dyn_array = LibDynArray()
 
  dyn_array.add(10)
  dyn_array.add(20)
  dyn_array.add(30)
  dyn_array.add(40)
 
  print("Length dyn array:", dyn_array.get_size())
 
  dyn_array.print_array()
 
  print('Set value by index')
  dyn_array.set_value(1, 25)
 
  dyn_array.print_array()
 
  print('Insert element by index')
  dyn_array.insert(35, 2)

  dyn_array.print_array()
 
  print('Delete element')
  dyn_array.remove()

  dyn_array.print_array()


def example_linked_list(): 
  myList = LinkedList()
  myList.append(10)
  myList.append(20)
  myList.append(30)
  myList.display()  

  # myList.remove(20)
  # myList.display() 


def example_dLinked_list():
  my_list = DLinkedList()
  # Add items to the beginning of the list using the push method
  my_list.push(1)
  my_list.push(2)
  my_list.push(3)

  # Add an item to the end of the list using the push_back method
  my_list.push_back(4)

  # Insert a new node after the node with value 2
  my_list.insert(my_list.start.next, 5)

  # Remove an item from the beginning of the list using the pop_front method
  # my_list.pop_front()

  # Now the list looks like this: 2 <-> 5 <-> 1 <-> 4

  # Remove an item from the end of the list using the pop_back method
  # my_list.pop_back()

  # Print
  my_list.print_list()

if __name__ == '__main__':
  example_dLinked_list()