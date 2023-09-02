from typing import TypeVar

T = TypeVar('T', bound='DLinkedList')

class Node:
    def __init__(self, x) -> None:
        self.x = x
        self.next = None
        self.prev = None

class DLinkedList:
    
    def __init__(self) -> None:
        self.start = None
        self.end = None

    # Операция добавления элемента в начало списка
    def push(self, x: int):
        t = Node(x)
        if self.start is None:
            # Если список пуст, новый элемент становится и начальным, и конечным
            self.start = t
            self.end = t
        else:
            # В противном случае, новый элемент становится начальным, а предыдущий начальный связывается с ним
            t.next = self.start
            self.start.prev = t
            self.start = t

    # Операция вставки элемента после указанного узла
    def insert(self, node: Node, x: int):
        t = Node(x)
        next = node.next
        if next is None:
            # Если следующего узла нет, то x становится новым конечным элементом
            t.next = None
            node.next = t
            t.prev = node
            self.end = t
        else:
            # Иначе, x вставляется между узлами node и next
            next.prev = t
            t.next = next
            node.next = t
            t.prev = node

    # Операция добавления элемента в конец списка
    def push_back(self, x: int):
        if self.end is None:
            # Если список пуст, x становится начальным и конечным элементом
            t = Node(x)
            self.start = t
            self.end = t
        else:
            # Иначе, x вставляется после текущего конечного элемента
            self.insert(self.end, x)

    # Операция удаления указанного узла из списка
    def delete(self, node: Node):
        prev = node.prev
        next = node.next
        if prev is not None:
            prev.next = next
        if next is not None:
            next.prev = prev
        node.next = None
        node.prev = None
        if node == self.start:
            # Если удаляется начальный элемент, обновляем начальный указатель
            self.start = next
        if node == self.end:
            # Если удаляется конечный элемент, обновляем конечный указатель
            self.end = node

    # Операция удаления первого элемента списка
    def pop_front(self):
        self.delete(self.start)
    
    # Операция удаления последнего элемента списка
    def pop_back(self):
        self.delete(self.end)

    # Операция вывода списка в порядке от начала к концу
    def print_list(self):
        current = self.start
        while current:
            print(current.x, end=" <-> ")
            current = current.next
        print("None")

    # Операция объединения двух списков
    def merge(self, l: T):
        if l.start is None:
            return
        if self.end is None:
            # Если текущий список пуст, просто делаем его равным переданному списку l
            self.start = l.start
            self.end = l.end
            return
        self.end.next = l.start
        l.start.prev = self.end
        self.end = l.end
