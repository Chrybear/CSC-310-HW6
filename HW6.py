# CSC 310 Homework 6
# Charles Ryan Barrett
# Python files taken/altered from course documents :


from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList
from heap_priority_queue import HeapPriorityQueue

#   Work area for problem 1

class SpQ(PriorityQueueBase):
    #  this class is based on the one given in priority queue lecture slide page 8

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        new = self._Item(k, v)
        walk = self._data.last()

        while walk is not None and new < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)
        else:
            self._data.add_after(walk, new)

    def min(self):
        if self.is_empty():
            print("The Priority queue is emtpy!")
        else:
            p = self._data.first()
            item = p.element()
            return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            print("Priority queue is empty!")
        else:
            item = self._data.delete(self._data.first())
            return item._key, item._value

    def __iter__(self):
        for item in self._data:
            yield item


def _insertsort(S):
    # First, put elements in sequence S into priority Queue
    pQ = SpQ()  # creating priority queue
    i = 0
    slen = len(S)
    while i < slen:   # This loop will add the values of S into pQ
        pQ.add(S[i], None)
        i += 1

    # this loop will add the now sorted elements back into S
    i = 0   # resetting i
    while i < slen:
        S[i] = pQ.remove_min()
        i += 1

    return S    # returning the now sorted sequence

# Work area for problem 2
def inplaceHS(L):
    # First, need to create a max-heap object
    mh = HeapPriorityQueue()
    # Then, populate it with the unsorted list
    x = 0
    while x < len(L):
        ke, el = L[x]
        mh.add(ke, el)
        x += 1
    # Now to create a sorted list to return
    L2 = []
    while not mh.is_empty(): # While heap still has values
        L2 = [mh.remove_max()] + L2 # Largest value at the end, smallest at the start
    return L2


# Work area for problem 3

class minheap(PriorityQueueBase):

    # Area taken from heap_priority_queue
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)  # recur at position of small child


    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def insert(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)  # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        item = self._data[0]
        return item._key

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)  # put minimum item at the end
        item = self._data.pop()  # and remove it from the list;
        self._downheap(0)  # then fix new root
        return (item._key, item._value)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._data:
            yield item  # yield the KEY

    # Area taken from heap_priority_queue.py end

def build_heap(L): # It made more sense to me to make the create min heap as an outside method
    h = minheap() # makes a new empty min heap
    i = 0
    while i < len(L):
        h.insert(L[i], None)
        i += 1
    return h


def build_heap_menu():
    go = True
    h = minheap()
    while go:
        print("1: Create a min heap")
        print("2: Insert a key into the min heap")
        print("3: How many items are currently in the min heap")
        print("4: Return the minimum value in the heap")
        print("5: Delete the min heap")
        print("6: Print the current min heap")
        print("0: Return to previous menu")
        print()
        inny = int((input("Choose: ")))

        if inny == 1:
            L = []
            makelist = True
            while makelist:
                k = int(input("Enter the key: "))
                # v = int(input("Enter the value for this key: "))
                L.append(k)
                print()
                endloop = input("Are you finished with the list y/n ?")
                if endloop.lower() == 'y':
                    makelist = False
            h = build_heap(L)  # Build the heap
            print()


        if inny == 2:
            k = int(input("Enter key: "))
            h.insert(k, None)
            print()
        if inny == 3:
            print("There are", h.__len__(), "items in the current heap")
            print()
        if inny == 4:
            print("The minimum value in the current heap is", h.min())
            print()
        if inny == 5:
            h.remove_min()
            print()
        if inny == 6:
            for x in h:
                print(x._key)
            print()
        if inny == 0:
            print()
            go = False


# p = SpQ()
# p.add(1, 'a')
# p.add(3, 'b')
# p.add(5, 'z')
# p.add(8, 'q')
# for i in p:
#     print(i)
# input area

go = True

while go:
    print("1: Enter unsorted sequence and have it sorted")
    print("2: Enter an unsorted list of keys for in-place heap-sort")
    print("3: Enter heap building menu")
    print("0: Exit the program")
    print()
    inny = int(input("Choose: "))
    if inny == 1:
        size = int(input("How large of a sequence?"))
        while size <= 0:
            print("Size must be greater than 0")
            size = int(input("How large of a sequence?"))
        seq = [None]*size
        i = 0
        while i < size:
            key = int(input("Enter key for this value:"))
            #elem = input("Enter an element for the sequence: ")
            print()
            seq[i] = key
            i += 1
        print("Your sequence: ")
        for q in seq:
            print(q)
        seq = _insertsort(seq)
        print()
        print("After sorting, it is: ")
        for q in seq:
            print(q[0])
        print()

    if inny == 2:
        li = []
        makeli = True
        while makeli:
            k = int(input("Enter key for this value: "))
            #val = input("Enter value for this key: ")
            li.append((k, None))
            endIt = input("Are you finished with the list y/n ?")
            if endIt.lower() == 'y':
                makeli = False
            print()
        # li = [(9,None), (7,None), (5,None), (2,None), (6,None), (4,None)]
        print("Your list is:")
        for q in li:
            print(q[0])
        print()
        print("After being sorted:")
        li = inplaceHS(li)
        for q in li:
            print(q[0])
        print()

    if inny == 3:
        print()
        build_heap_menu()

    if inny == 0:
        print("Goodbye!")
        go = False




