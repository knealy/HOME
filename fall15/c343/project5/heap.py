from swap import swap

def less(x, y):
    return x < y

def less_key(x, y):
    return x.key < y.key

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * (i + 1)

def parent(i):
    return (i-1) / 2

# Student code -- fill in all the methods that have pass as the only statement
class Heap:
    def __init__(self, data, less = less):
        self.data = data
        self.less = less
        self.heap_size = 0
        self.build_min_heap()

    def __repr__(self):
        return repr(self.data)
    
    def minimum(self):
        return self.data[0]

    def insert(self, obj):
        #print self.data
        self.data.append(obj)
        self.heap_size += 1
        self.build_min_heap()
        
    def extract_min(self):
        assert self.heap_size != 0
        heap_min = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        self.heap_size -= 1
        self.min_heapify(0)
        return heap_min
        
    def min_heapify(self, i):
        H = self.data
        n = len(H)
        # which of i, left or right is smallest?
        if left(i) < n and H[i].key > H[left(i)].key:
            smallest = left(i)
        else:
            smallest = i
        if right(i) < n and H[smallest].key > H[right(i)].key:
            smallest = right(i)
        if smallest != i:
            swap(H, i, smallest)
            self.min_heapify(smallest)
        
    def build_min_heap(self):
        last_parent = (self.heap_size/2)-1        # middle element
        for i in range(last_parent,-1,-1):               
            self.min_heapify(i)

class PriorityQueue:
    def __init__(self, less=less_key):
        self.heap = Heap([], less)  # self.data=[],self.less=less_key, self.build_min_heap() 

    def __repr__(self):
        return repr(self.heap)

    def push(self, obj):
        self.heap.insert(obj)

    def pop(self):
        return self.heap.extract_min()


if __name__ == "__main__":
    # unit tests here
    # Huffman Tree node
    class HTreeNode:
        def __init__(self, key=None, char=None):
            self.key = key
            self.char = char
            self.left = None
            self.right = None
        
        def __repr__(self):
            return repr(self.char) + ': ' + repr(self.key)

    n1 = HTreeNode()
    n1.key = 5
    n1.char = 'a'
    n2 = HTreeNode()
    n2.key = 3
    n2.char ='b'
    n3 = HTreeNode()
    n3.key = 2
    n3.char ='c'
    n4 = HTreeNode()
    n4.key = 10
    n4.char ='d'
    n5 = HTreeNode()
    n5.key = 1
    n5.char ='e'

    # # n6 = HTreeNode()
    # n6.key = 6
    # n7 = HTreeNode()
    # n7.key = 16
    # n8 = HTreeNode()
    # n8.key = 4
    
    H = Heap([],less_key)
    H.insert(n1)
    H.insert(n2)
    H.insert(n3)    
    H.insert(n4)
    H.insert(n5)
    # H.insert(n6)
    # H.insert(n7)
    # H.insert(n8)

    print H.data[2].key == 3
    print H.extract_min().key == 1
    print H.minimum().key == 2
    print H