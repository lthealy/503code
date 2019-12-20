#%% This chunk will define all the necessary functions and classes

# Classes and features: Node and DoubleLink: _length, is_empty, get_item, set_item, insert_at_end, print_list, list_indices
# Functions: sparsify(vec) and sparse_math(vec1,vec2,op)

class Node:
    ''' Node class for implementation in a DLL with 4 slots
    
    _element = the value stored in the node
    _prev = the prior node
    _next = the node that follows
    _index = the index of _element within the initial dense vector
    
    '''
    __slots__ = '_element','_prev','_next','_index'

    def __init__(self,element,index, prev = None,next = None):
        self._element = element
        self._index = index
        self._prev = prev
        self._next = next

# Define a DLL
class DoubleLink:
    ''' Doubly Linked List representation of a sparse vector with 3 slots
    
    _head
    _tail
    _size
    
     '''
    class Node:
        __slots__ = '_element','_prev','_next','_index'

        def __init__(self,element,index, prev = None,next = None):
            self._element = element
            self._index = index
            self._prev = prev
            self._next = next
            
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def _length(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def insert_at_end(self, element, index):
        new_node = Node(element, index)
        if self.is_empty() == True:
            self._head = new_node
            self._size =+ 1
            self._tail = new_node
        else:
            if index < self._tail._index:
                return 'Index is lower than current tail index'
            self._tail._next = new_node
            new_node._prev = self._tail
            self._tail = new_node
            self._tail._next = None 
            self._size =+ 1

    def print_list(self):
        if self.is_empty() == True:
            print('No nodes')
        else:
            n = self._head
            while n is not None:
                print('value: ', n._element, 'index: ', n._index)
                n = n._next

    def get_item(self,index):
        if self.is_empty() == True:
            print('No nodes')
        else:
            n = self._head
            while n._index != index:
                n = n._next
                if index > n._index:
                    return 'Index not found'
            print('value: ', n._element, 'index: ', n._index)
            return n

    def set_item(self,element,index):
        if self.is_empty() == True:
            print('No nodes')
        else:
            n = self.get_item(index)
            n._element = element
            print('New value: ', n._element, 'New index: ', n._index)

    def list_indices(self):
        if self.is_empty() == True:
            print('No nodes')
        else:
            n = self._head
            indices = []
            while n is not None:
                indices.append(n._index)
                n = n._next
            print(indices)
            return indices

    def insert(self,element,index):
        new_node = Node(element, index)
        if self.is_empty() == True:
            self._head = new_node
            self._size =+ 1
            self._tail = new_node
        else:
            n = self._head
            while n._index < new_node._index and n._next is not None:
                if n._next._index > new_node._index:
                    new_node._prev = n
                    new_node._next = n._next
                    n._next = new_node
                    n._next._prev = new_node
                    self._size =+ 1
            # add at end
            if n._next is None:
                self._tail._next = new_node
                new_node._prev = self._tail
                self._tail = new_node
                self._tail._next = None 
                self._size =+ 1
        return
                
            

# Convert a list into a sparse representation DLL
def sparsify(vec):
    tmp = DoubleLink()
    for i in range(len(vec)):
        if vec[i] == 0:
            continue
        else:
            tmp.insert_at_end(element = vec[i], index = i)
    return tmp

# Perform Addition, Subtraction, or Dot Product Calculations on two lists or sparse vectors
# Note: Lists will be automatically converted to sparse vectors
def sparse_math(vec1, vec2, op):
    # if inputs are not sparse DLL yet, sparsify them
    if type(vec1) == list:
        vec1 = sparsify(vec1)
    if type(vec2) == list:
        vec2 = sparsify(vec2)
    # set start points as head of each input
    x = vec1._head
    y = vec2._head
    if op in ['dot','mult','*']:
        z = 0
        print('Sparse Dot Product will be returned as single value')
        while x is not None and y is not None:
            if x._index == y._index:
                z += (x._element * y._element)            
                x = x._next; y = y._next
            elif x._index < y._index:
                x = x._next
            elif x._index > y._index:
                y = y._next
        return z
    if op in ['+','sum','add']:
        print('Sparse Vectors will be added and returned as a sparse DLL')
        z = []
        while x is not None and y is not None:
            if x._index == y._index:
                z.append(x._element + y._element)            
                x = x._next; y = y._next
            elif x._index < y._index:
                z.append(x._element)
                x = x._next
            elif x._index > y._index:
                z.append(y._element)
                y = y._next
        print("Dense: ", z)
        z = sparsify(z)
        print("Sparse: ")
        z.print_list()
        return z
    if op in ['-','subtract','sub']:
        print('Sparse Vectors will be subtracted and returned as a sparse DLL')
        z = []
        while x is not None and y is not None:
            if x._index == y._index:
                z.append(x._element + y._element)            
                x = x._next; y = y._next
            elif x._index < y._index:
                z.append(x._element)
                x = x._next
            elif x._index > y._index:
                z.append(y._element)
                y = y._next
        print("Dense: ", z)
        z = sparsify(z)
        print("Sparse: ")
        z.print_list()
        return z

#%% Validate sparsify and bound operators of DoubleLink

# Create a dense list
vec1 = [0,0,8,0,4,0]

# Validate functions
print('--- Dense list ---')
print(vec1)
vec1 = sparsify(vec1)
#print_list will list out every value and index present in sparse mode
print('--- print_list output ---')
vec1.print_list()

#list_indices will list only the non-zero indices, no values
print('--- list_indices output ---')
vec1.list_indices()

# call one node using a listed index
print('--- get_item output ---')
vec1.get_item(2)

# Change that value
print('--- set_item output ---')
vec1.set_item(10,2)

# Add a value at end (will also initialize if its an empty DoubleLink)
print('--- print_list after insert_at_end ---')
vec1.insert_at_end(12,6)
vec1.print_list()

# Try to insert at end with an index lower than the current _tail
print('--- Try to insert at end with an index lower than the current _tail ---')
vec1.insert_at_end(12,5)

# Use insert to add anywhere
vec1.insert(4,3)
vec1.print_list()

#%% Sample Flow 2

# Create two dense lists - in this case, not all indices agree but _length of both is equivalent
vec1 = [0,0,1,0,2,0,0,0,0,7,8,2,5]
vec2 = [0,0,2,0,1,0,0,1,5,0,0,4,2]
