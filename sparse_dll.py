class Node:
        __slots__ = '_element','_prev','_next'

        def __init__(self,element,prev = None,next = None):
            self._element = element
            self._prev = prev
            self._next = next

class DoubleLink:
    class Node:
        __slots__ = '_element','_prev','_next'

        def __init__(self,element,prev = None,next = None):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def insert_at_start(self, element):
        new_node = Node(element)
        if self.is_empty() == True:
            self._head = new_node
            self._size =+ 1
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node
    
    def traverse_list(self):
        if self.is_empty() == True:
            print('No nodes')
        else:
            n = self._head
            while n is not None:
                print(n._element)
                n = n._next

    def insert(self,element,prev_node,next_node):
        if self.is_empty == True:
            new_node = Node(element)
            self._head = new_node
            self._size =+ 1
        else:
            new_node = Node(element)


tmp = DoubleLink()
tmp.traverse_list()
tmp.insert_at_start(4)
tmp.traverse_list()
tmp.insert_at_start(8)
tmp.traverse_list()

            

            






