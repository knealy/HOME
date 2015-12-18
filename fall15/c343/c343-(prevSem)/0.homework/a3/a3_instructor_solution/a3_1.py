#--- Part I: finish the implementation of this class 

from lec4 import * 

class MutableList :

  """Mutable lists. We maintain a pointer 'front' to a list and use DELEGATION
  for read-only operations. Operations that change the list are implemented by
  explicit pointer manipulations that update 'front' or self.tail for the relevant
  node in the list.
  """

  def __init__ (self) :
    self.front = EmptyList()

  #- easy delegations

  def search (self,v) :
    """Returns True or False depending on whether 'v' occurs in the current list or not.
    >>> xs = MutableList()
    >>> xs.search(1)
    False
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> xs.add(4)
    >>> xs.search(2)
    True
    >>> xs.search(10)
    False
    """
    return self.front.search(v)

  def isEmpty (self) :
    """Returns True or False depending on whether the current list is empty or not.
    >>> xs = MutableList()
    >>> xs.isEmpty()
    True
    >>> xs.add(1)
    >>> xs.isEmpty()
    False
    """
    return self.front.isEmpty()

  def size (self) :
    """O(n).
    Return the number of the elements in the current list.
    >>> xs = MutableList()
    >>> xs.size()
    0
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> xs.add(4)
    >>> xs.size()
    4
    """
    return self.front.size()

  def index (self,v) :
    """Return the index of the first occurrence of 'v' in the current list.
    Raises NotFoundE if 'v' does not occur.
    """
    return self.front.index(v)

  #-- insertion methods

  def add (self,v) :
    """Adds 'v' at the front of the list.
    >>> xs = MutableList()
    >>> print xs
    []
    >>> xs.add(1)
    >>> print xs
    1, []
   >>> xs.add(2)
    >>> print xs
    2, 1, []
    """
    self.front = self.front.add(v)

  def append (self,v) :
    """Adds 'v' to the end of the current list.
    >>> xs = MutableList()
    >>> print xs
    []
    >>> xs.append(0)
    >>> print xs
    0, []
    >>> xs = MutableList()
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> xs.add(4)
    >>> print xs
    4, 3, 2, 1, []
    >>> xs.append(10)
    >>> print xs
    4, 3, 2, 1, 10, []
    """
    temp = Node(v,EmptyList())
    if self.isEmpty() :
      self.front = temp
    else : 
      last = self.front.drop(self.size() - 1)
      last.tail = temp

  def insert (self,i,v) :
    """Inserts 'v' in zero-based position 'i'. Raises an IndexOutOfBoundsE exception
    if 'i' is out of bounds.
    >>> xs = MutableList()
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> xs.add(4)
    >>> xs.add(5)
    >>> xs.add(6)
    >>> print xs
    6, 5, 4, 3, 2, 1, []
    >>> xs.insert(2,100)
    >>> print xs
    6, 5, 100, 4, 3, 2, 1, []
    >>> xs = MutableList()
    >>> try :
    ...   xs.insert(100,5)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    >>> xs = MutableList()
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> print xs
    3, 2, 1, []
    >>> xs.insert(3,10)
    >>> print xs
    3, 2, 1, 10, []
    >>> xs = MutableList()
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> try :
    ...   xs.insert(4,100)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    """
    if i == 0 :
      self.add(v)
    else :
      current = self.front.drop(i-1)
      if current.isEmpty() :
        raise IndexOutOfBoundsE()
      current.tail = Node(v,current.tail)

  #-- remove methods

  def remove (self,v) :
    """Removes the first node containing 'v' from the current list. If there is
    no such node the method has no effect.
    >>> xs = MutableList()
    >>> xs.remove(1)
    >>> print xs
    []
    >>> xs.add(1)
    >>> xs.remove(1)
    >>> print xs
    []
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> print xs
    3, 2, 1, []
    >>> xs.remove(10)
    >>> print xs
    3, 2, 1, []
    >>> xs.remove(2)
    >>> print xs
    3, 1, []
    >>> xs.remove(1)
    >>> print xs
    3, []
    >>> xs.remove(3)
    >>> print xs
    []
    """
    if self.isEmpty() :
      return None
    if self.front.head == v :
      self.front = self.front.tail
      return None
    previous = self.front
    current = self.front.tail
    while not current.isEmpty() and current.head != v :
      previous = current
      current = current.tail
    if current.isEmpty() : return None
    previous.tail = current.tail

  def pop (self, i=None) : 
    """Removes the element at index 'i' or the last element if no index is given.
    >>> xs = MutableList()
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> print xs
    3, 2, 1, []
    >>> xs.pop()
    1
    >>> print xs
    3, 2, []
    >>> xs.pop()
    2
    >>> print xs
    3, []
    >>> xs.pop()
    3
    >>> print xs
    []
    >>> try :
    ...   xs.pop()
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    >>> xs = MutableList()
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> xs.pop(0)
    3
    >>> print xs
    2, 1, []
    >>> xs.add(3)
    >>> xs.add(4)
    >>> xs.add(5)
    >>> xs.pop(2)
    3
    >>> print xs
    5, 4, 2, 1, []
    >>> try :
    ...   xs.pop(100)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    >>> xs = MutableList()
    >>> try :
    ...   xs.pop(0)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    """
    if i == None : i = self.size() - 1
    if i == 0 :
      if self.isEmpty() :
        raise IndexOutOfBoundsE()
      else :
        d = self.front.head
        self.front = self.front.tail
        return d
    else : 
      current = self.front.drop(i-1)
      if current.tail.isEmpty() :
        raise IndexOutOfBoundsE()
      else :
        d = current.tail.head
        current.tail = current.tail.tail
        return d

  def rotate(self) :
      """Rotates a list one element to the right.
      >>> xs = MutableList()
      >>> xs.add(1)
      >>> xs.add(2)
      >>> xs.add(3)
      >>> xs.add(4)
      >>> print xs
      4, 3, 2, 1, []
      >>> xs.rotate()
      >>> print xs
      1, 4, 3, 2, []
      """
      d = self.pop()
      self.add(d)

  def __str__ (self) :
    return str(self.front)

#-----------------------------------------------------------------------------

if __name__ == "__main__" :
  import doctest
  doctest.testmod()

