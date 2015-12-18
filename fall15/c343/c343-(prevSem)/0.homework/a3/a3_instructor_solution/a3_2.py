#--- Part II: implement stacks using mutable lists; implement queues using two stacks

from a3_1 import * 

class Stack :
    """
    >>> s = Stack()
    >>> s.isEmpty()
    True
    >>> s.push(4)
    >>> s.push('dog')
    >>> s.peek()
    'dog'
    >>> s.push(True)
    >>> s.size()
    3
    >>> s.isEmpty()
    False
    >>> s.push(8.4)
    >>> s.pop()
    8.4
    >>> s.pop()
    True
    >>> s.size()
    2
    """

    def __init__ (self) :
        self.stack = MutableList()

    def isEmpty (self) :
        return self.stack.isEmpty()

    def size (self) :
        return self.stack.size()

    def push (self, v) :
        self.stack.add(v)

    def pop (self) :
        return self.stack.pop(0)

    def peek (self) :
        d = self.stack.pop(0)
        self.stack.add(d)
        return d


class Queue :
    """
    >>> q = Queue()
    >>> q.isEmpty()
    True
    >>> q.enqueue(4)
    >>> q.enqueue('dog')
    >>> q.enqueue(True)
    >>> q.size()
    3
    >>> q.isEmpty()
    False
    >>> q.dequeue()
    4
    >>> q.enqueue(8.4)
    >>> q.dequeue()
    'dog'
    >>> q.dequeue()
    True
    >>> q.dequeue()
    8.4
    >>> q.size()
    0
    """
    def __init__ (self) :
      self.front = Stack()
      self.back = Stack()
    
    def isEmpty (self) :
        return self.front.isEmpty() and self.back.isEmpty()

    def size (self) :
        return self.front.size() + self.back.size()

    def enqueue (self, v) :
        self.front.push(v)

    def dequeue (self) :
        if self.back.isEmpty() :
            while not self.front.isEmpty() :
                self.back.push(self.front.pop())
        return self.back.pop()

if __name__ == "__main__" :
  import doctest
  doctest.testmod()
