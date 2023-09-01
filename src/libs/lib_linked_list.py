class Node:
    def __init__(self, x) -> None:
        self.x = x
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, x):
        node = Node(x)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def remove(self, x):
        if self.head is None:
            return

        if self.head.x == x:
            self.head = self.head.next
            return

        current = self.head

        while current.next and current.next.x != x:
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        current = self.head

        while current:
            next_node = current.next if current.next else None
            print(f"current: {current.x}, next: {next_node.x if next_node else 'None'}")
            current = current.next