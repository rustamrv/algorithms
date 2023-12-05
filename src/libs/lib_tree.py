

class Node:
    
    def __init__(self, x, parent) -> None:
        self.x = x
        self.parent = parent
        self.l = None
        self.r = None


class LibTree:
    
    def __init__(self) -> None:
        self.root = None

    def add_Node(self, v: Node, x: int):
        if v is None:
            return
        if x < v.x:
            if v.l is None:
                v.l = Node(x, v)
                return
            self.add_Node(v.l, x)
        else:
            if v.r is None:
                v.r = Node(x, v)
                return
            self.add_Node(v.r, x)


    def add(self, x):
        if self.root is None:
            self.root = Node(x, None)
        else:
            self.add_Node(self.root, x)

    def find(self, v: Node, x):
        if x is None:
            return v
        if v.x > x:
            return self.find(v.l, x)
        return self.find(v.r, x)

    def deleteNode(self, v: Node):
        if v is None: 
            return
        if (v.l is None) or (v.r is None):
            child: Node = None
            if not v.l is None:
                child = v.l
            else:
                child = v.r
            if v == self.root:
                self.root = child
                if not child is None:
                    child.parent = None
            if v.parent.l == v:
                v.parent.l = child

    def delete(self, x):
        if self.root is None:
            return
        t = self.find(self.root, x)
        if t is None:
            return
        self.deleteNode(t)

    def print(self, v: Node):
        if v == None:
            return
        self.print(v.l)
        print('Element', v.x)
        self.print(v.r)