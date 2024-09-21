class Heap:
    def __init__(self):
        self.heap =[]
        self.size =0


    def insert(self, val):
        self.heap.append(val)
        self.size +=1
        self.shiftup(self.size)


    def shiftup(self, s):
        i =s-1
        while i>0:
            if self.heap[i]>self.heap[(i-1)//2]:
                temp =self.heap[i]
                self.heap[i] =self.heap[(i-1)//2]
                self.heap[(i-1)//2] =temp
            else:
                break
            i =(i-1)//2
    def deleteMax(self):
        if len(self.heap)==0:
            raise Exception("Empty Heap")
        self.heap[0] =self.heap[-1]
        self.heap.pop()
        self.size -=1
        
        self.shiftdown(0)
    def display(self):
        print(self.heap)

    def shiftdown(self, i):
        while (i*2)<self.size-1:              
            if (i*2)+2>=self.size:
                if(i*2)+1>=self.size:
                    break
                else:
                    v =self.heap[(i*2)+1]
            else:
                    v = max(self.heap[i*2 +1], self.heap[i*2 +2 ])
            if self.heap[i]<v:         
                j =self.heap.index(v)
                temp =self.heap[i]
                self.heap[i] =self.heap[j]
                self.heap[j] =temp
            else:
                break
            i =j
           

    def findMax(self):
        if len(self.heap)==0:
            raise Exception("Empty Heap")
        return self.heap[0]
    def extractMax(self):
        if len(self.heap)==0:
            raise Exception("Empty Heap")
        v =self.heap[0]
        self.deleteMax()
        return v
    
    def isEmpty(self):
        return len(self.heap)==0
    def clear(self):
        self.heap = []
        self.size =0
    def heap_size(self):
        return self.size
    def deleteKey(self, i):
        self.heap[i] =self.heap[-1]
      
        self.heap.pop()
        self.size -=1
        self.shiftdown(i)

    def increase_key(self, i, delta):
        self.heap[i] =self.heap[i] + delta
        self.shiftup(i+1)
    def decrease_key(self, i, delta):
        self.heap[i] =self.heap[i] - delta
        self.shiftdown(i)
    def display(self):
        print(self.heap)
    def build_heap(self, arr):
        for i in arr:
            self.insert(i)

    def sort(self):
        v =self.size
        for i in range(v):
            temp =self.heap[0]
            self.heap[0] =self.heap[self.size-1]
            self.heap[self.size-1] =temp
            self.size -=1
            self.shiftdown(0)
        self.size =v

    def build_heapone(self):
        i =int(len(self.heap)//2)-1
        while i>=0:
            self.shiftdown(i)
            i -=1


    def heap_sort(self, arr):
        #heapify --to build max/min heap from array
        self.heap =arr
        self.size =len(self.heap)
        self.build_heapone()
       
        self.sort()
      
        


    
def main():
    h =Heap()
    h.heap_sort([40, 90, 70, 80, 30, 20, 60, 50])
    h.display()






main()
                


