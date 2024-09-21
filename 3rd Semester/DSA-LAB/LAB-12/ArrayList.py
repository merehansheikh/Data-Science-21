# array based version of linked nodes based code in doubly-LL5.py
class ArrayList:
#    class Node: not required for array based list, delete this line





    class ALIterator:
        def __init__(self, index=0, list=None):
            self.current = index-1
            self.list = list
        def __eq__( self, rhs ):
            return self.current == rhs.current
        def __ne__( self, rhs ):
            return self.current != rhs.current
        def getObject( self ):
            return self.list.Array[self.current]
        def __iter__(self):  # this is not mandatory, why
            return self        
        def __next__( self ):
            if self.current != self.list.ALSize-1:
                self.current = self.current + 1
                return self
            else:
                raise StopIteration


    class ALRIterator:
        def __init__(self, index, list=None):
            self.current = index+1
            self.list = list
        def __eq__( self, rhs ):
            return self.current == rhs.current
        def __ne__( self, rhs ):
            return self.current != rhs.current
        def getObject( self ):
            return self.list.Array[self.current]
        def __iter__(self):  # this is mandatory, why
            return self        
        def __next__( self ):
            if self.current != 0:
                self.current = self.current - 1
                return self
            else:
                raise StopIteration


    def __init__(self, ARSize = 100):
        self.ARSize=ARSize
        self.ALSize=0
        self.Array=[None]*self.ARSize


    def __iter__(self):
        return self.ALIterator(0, self)  # index 0 is the locations of FIRST object in array

    def __reversed__(self):
        return self.ALRIterator(self.ALSize-1, self)  # index 0 is the locations of LAST object in array

    def begining(self):
        return self.ALIterator(0, self)

    def end(self):
        return self.ALIterator(self.ALSize, self)

    def rbegining(self):
        return self.ALRIterator(self.ALSize-1, self)

    def rend(self):
        return self.ALRIterator(-1, self)

    def isFull(self):
        return self.ALSize == self.ARSize

    def isEmpty(self):
        return self.ALSize == 0

    def size(self):
        return self.ALSize

    def append(self,o):
        if not self.isFull():
            self.Array[self.ALSize] = o
            self.ALSize = self.ALSize + 1



    def remove(self, index):
        if type(index) is self.ALIterator:
            index = index.current
        if index < 0 or index >= self.ALSize:
            raise Exception("Invalid Index")
        j = index
        while j < self.ALSize:
            self.Array[j] = self.Array[j+1]
            j = j + 1
        self.ALSize = self.ALSize - 1


    def set(self, index, o):
        pass
        # assign o at index in array

    def Display(self):
        j = 0
        while j < self.ALSize:
            print(self.Array[j])
            j = j + 1
        print()

def main():
    # Create a new Doubly Linked List
    AL = ArrayList()
    # Insert the element to empty list
    AL.append(10)
    # Insert the element at the end
    AL.append(20)
    AL.append(30)
    AL.append(70)
    AL.append(50)
    AL.append(60)
    AL.append(80)
    AL.append(90)
    AL.append(40)
    # Display Data
    print("Display 10 items")
    AL.Display()
    # Delete elements from start
    AL.remove(0)
    # Delete elements from end
    AL.remove(0)
    # Display Data
    print("Display without (removed) first two items")
    AL.Display()
    print()

    print("OUTPUT of 'for d in AL:'")
    for d in AL:
        print(d.getObject())
    print()

    print("OUTPUT of 'for d in reversed(AL):'")
    for d in reversed(AL):
        print(d.getObject())
    print()

    print("OUTPUT through manual next calls")
    itm1 = iter(AL)
    itm2 = AL.begining()

    print("first through itm1: " + str(next(itm1).getObject()))
    print("next  through itm1: " + str(next(itm1).getObject()))
    print("first through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm1: " + str(next(itm1).getObject()))
    print("Removing current data")
    AL.remove(itm1)
    print("Removed")
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    # due to remove above, print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm1: " + str(next(itm1).getObject()))

    print()

    print("OUTPUT through beginning and end")
    i = AL.begining()
    while i != AL.end():
        i = next(i)
        print(i.getObject())
    print()

    print("OUTPUT through rbeginning and rend")
    i = AL.rbegining()
    while i != AL.rend():
        t = next(i)
        print(t.getObject())
    print()

main()

