from libs import *
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
  # my_list.push(3)

  # Add an item to the end of the list using the push_back method
  my_list.push_back(4)

  # Insert a new node after the node with value 2
  # my_list.insert(my_list.start.next, 5)

  # Remove an item from the beginning of the list using the pop_front method
  # my_list.pop_front()

  # Now the list looks like this: 2 <-> 5 <-> 1 <-> 4

  # Remove an item from the end of the list using the pop_back method
  # my_list.pop_back()

  # Print
  my_list.print_list()

def example_queue():
  # Создаем очередь с максимальным размером 5
  my_queue = LibQueue(5)

  # Проверяем, пуста ли очередь
  print("Очередь пуста?", my_queue.empty())

  # Добавляем элементы в очередь
  my_queue.enqueue(1)
  my_queue.enqueue(2)
  my_queue.enqueue(3) 
  # Проверяем первый элемент в очереди (без удаления)
  print("Первый элемент в очереди:", my_queue.peek())

  # Извлекаем элементы из очереди
  item1 = my_queue.dequeue()
  item2 = my_queue.dequeue()

  print("Извлеченные элементы:", item1, item2)

  # Проверяем, пуста ли очередь после извлечения
  print("Очередь пуста?", my_queue.empty())

def example_sorted():
    lib_sort = LibSort([5,1,3,2,2,4,6,8])
    print(lib_sort.data)

    lib_sort.merge_sort(lib_sort.data)
    print(lib_sort.data)


def example_recursion():
  lc = LibRecursion([0] * 4)
  lc.gen(0, 4)

def example_bit():
  b = Bitset(5)
  def gen(x: int, n: int, k: int):
    if n - x < k:
      return
    if x == n:
      for i in range(0, n):
        print(f'Bit {i}: {b.get(i)}')
      return
    b.set_value(x, 0)
    gen(x + 1, n, k)
    b.set_value(x, 1)
    gen(x + 1, n, k - 1)
  gen(0,5,3)


def hanoi(n: int, fr: str, to: str, aux: str):
  if n == 1:
    print('Move from ' + fr + ' to ' + to)
    return
  hanoi(n - 1, fr, aux, to)
  print('Move from ' + fr + ' to ' + to)
  hanoi(n - 1, aux, to, fr)


def example_honoi():
  hanoi(3, 'A', 'C', "B")


if __name__ == '__main__':
  example_sorted()