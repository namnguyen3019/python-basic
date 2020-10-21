class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def hasLeftChild(self, i):
        return (2*i+1) < len(self.heap)
    def hasRightChild(self, i):
        return (2*i+2) < len(self.heap)
    def leftChild(self, i):
        if self.hasLeftChild(i):
            return self.heap[2*i+1]
        else:
            return None
    def rightChild(self, i):
        if self.hasRightChild(i):
            return self.heap[2*i+2]
        else:
            return None
    def indexOfParent(self, i):
        if i > 0 :
            return (i-1)//2
        else:
            return None

    def heapifyUp(self, i):    
        while (i+1) //2 > 0:
            if self.heap[i] < self.heap[(i-1)//2]:
                self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def heappush(self, val):
        self.heap.append(val)
        self.size += 1
        self.heapifyUp(len(self.heap)-1)
    
    def heapifyDown(self, i):

        while (i*2+1) < len(self.heap):
            smallerItem = self.leftChild(i)
            idx = (2*i + 1)
            if(self.hasRightChild(i) and self.rightChild(i) < self.leftChild(i)):
                smallerItem = self.rightChild(i)
                idx = (2*i + 2)
            if self.heap[i] < smallerItem: break
            else:
                self.heap[i], self.heap[idx] = self.heap[idx], self.heap[i]
                i = idx

    def heappop(self):
        remove_item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapifyDown(0)
        return remove_item

    def heappushpop(self, val):
        self.heappush(val)
        self.heappop()

    def heapreplace(self, item):
        self.heappop()
        self.heappush(item)

    def nlargest(self, n):
        # ????
        tempHeap = self.heap
        while len(self.heap) > n:
            self.heappop()
        output = self.heap
        self.heap = tempHeap
        return output

    def nsmallest(self, n):
        output = []
        while len(output) < n:
            x = self.heappop()
            output.append(x)
        return output

if __name__=="__main__":
    heap = MinHeap()
    heap.heappush(1)
    heap.heappush(0)
    heap.heappush(2)
    heap.heappush(-1)
    heap.heappush(3)

    for i in range(len(heap.heap)):
        print(heap.heap[i])

    nlargest = heap.nlargest(2)
    print('n largest ', nlargest)

    print('heap after nlargest')
    for i in range(len(heap.heap)):
        print(heap.heap[i])
    nsmallest = heap.nsmallest(2)
    print('n smallest ', nsmallest)
    