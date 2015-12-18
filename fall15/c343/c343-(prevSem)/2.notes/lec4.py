# non-mutable; persistent linked lists; also a stack
# immutable collections are much easier to use concurrently
#
# NOTE: There are no assignments to self.tail after its initialization
#

class EmptyListE :
  def __str__(self) :
    return "Exception: list is empty"

class NotFoundE :
  def __str__(self) :
    return "Exception: element not found"

class IndexOutOfBoundsE :
  def __str__(self) :
    return "Exception: index out of bounds"

#---

class List :

  """Non-mutable persistent lists
  >>> xs = EmptyList().add(1).add(2).add(3).add(4)
  >>> print xs
  4, 3, 2, 1, []
  >>> ys = xs.append(100)
  >>> print ys
  4, 3, 2, 1, 100, []
  >>> print xs
  4, 3, 2, 1, []
  """

  def size (self) :
    """O(n).
    Returns the number of elements in the current list.
    >>> EmptyList().size()
    0
    >>> EmptyList().add(1).add(2).add(3).size()
    3
    """
    pass

  def isEmpty (self) :
    """O(1).
    Returns True or False depending on whether the current list is empty or not.
    >>> EmptyList().isEmpty()
    True
    >>> EmptyList().add(1).add(2).add(3).isEmpty()
    False
    """
    pass

  def search (self, v) :
    """O(n).
    Returns True or False depending on whether 'v' occurs in the current list or not.
    >>> EmptyList().search(1)
    False
    >>> EmptyList().add(1).add(2).add(3).search(2)
    True
    >>> EmptyList().add(1).add(2).add(3).search(100)
    False
    """
    pass

  def elem (self, i) :
    """O(n).
    Returns the element at zero-based index 'i' in the current list. If 'i' is out
    of bounds, raises an exception.
    >>> try :
    ...   EmptyList().elem(0)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    >>> try :
    ...   EmptyList().add(1).add(2).add(3).elem(10)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    >>> EmptyList().add(1).add(2).add(3).elem(0)
    3
    >>> EmptyList().add(1).add(2).add(3).elem(1)
    2
    >>> EmptyList().add(1).add(2).add(3).elem(2)
    1
    """
    pass

  def index (self, v) :
    """O(n).
    Returns the zero-based index of the first occurrence of 'v' in the current
    list. If 'v' does not occur in the list, raises NotFoundE exception.
    >>> try :
    ...   EmptyList().index(1)
    ... except NotFoundE :
    ...   print 'Not found'
    ...
    Not found
    >>> EmptyList().add(1).add(2).add(3).index(3)
    0
    >>> EmptyList().add(1).add(2).add(3).index(2)
    1
    >>> EmptyList().add(1).add(2).add(3).index(1)
    2
    >>> try :
    ...   EmptyList().add(1).add(2).add(3).index(10)
    ... except NotFoundE :
    ...   print 'Not found'
    ...
    Not found
    """
    pass
    
  def insert(self, i, v) :
    """O(n).
    Inserts 'v' at the given zero-based index 'i'. If the index i is too large,
    throw IndexOutOfBoundsE exception.
    >>> str (EmptyList().insert(0,5))
    '5, []'
    >>> try :
    ...   EmptyList().insert(100,5)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    >>> str (EmptyList().add(1).add(2).add(3).insert(0,100))
    '100, 3, 2, 1, []'
    >>> str (EmptyList().add(1).add(2).add(3).insert(1,100))
    '3, 100, 2, 1, []'
    >>> str (EmptyList().add(1).add(2).add(3).insert(2,100))
    '3, 2, 100, 1, []'
    >>> str (EmptyList().add(1).add(2).add(3).insert(3,100))
    '3, 2, 1, 100, []'
    >>> try :
    ...   str (EmptyList().add(1).add(2).add(3).insert(4,100))
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    """
    pass

  def remove(self,v) :
    """O(n).
    Remove the first occurrence (if any) of 'v' from the current list.
    >>> str(EmptyList().remove(10))
    '[]'
    >>> str(EmptyList().add(1).add(2).add(3).remove(2))
    '3, 1, []'
    >>> str(EmptyList().add(2).add(2).add(3).remove(2))
    '3, 2, []'
    """
    pass

  def append(self,v) :
    """O(n).
    Inserts 'v' at the end of the current list.
    >>> str(EmptyList().append(10))
    '10, []'
    >>> str(EmptyList().add(1).add(2).add(3).append(10))
    '3, 2, 1, 10, []'
    >>> xs = EmptyList().add(1).add(2).add(3)
    >>> print xs
    3, 2, 1, []
    >>> print xs.append(10)
    3, 2, 1, 10, []
    >>> print xs
    3, 2, 1, []
    """
    pass

  def drop(self,i) : 
    """Drops the first 'i' elements and returns the remaining list; raises an
    exception if the index is too large.
    >>> xs = EmptyList().add(1).add(2).add(3).add(4)
    >>> print xs.drop(0)
    4, 3, 2, 1, []
    >>> print xs.drop(1)
    3, 2, 1, []
    >>> print xs.drop(2)
    2, 1, []
    >>> print xs.drop(3)
    1, []
    >>> print xs.drop(4)
    []
    >>> try :
    ...   xs.drop(5)
    ... except IndexOutOfBoundsE as e :
    ...   print e
    ...
    Exception: index out of bounds
    """
    pass

  def add(self,v) :
    """O(1).
    Inserts 'v' at the front of the list.
    >>> str(EmptyList().add(1).add(2).add(3))
    '3, 2, 1, []'
    """
    return Node(v,self)

  def __iter__ (self) :
    """Creates an iterator.
    >>> it = iter(EmptyList().add(1).add(2).add(3))
    >>> it.next()
    3
    >>> it.next()
    2
    >>> it.next()
    1
    >>> try :
    ...   it.next()
    ... except StopIteration :
    ...   print 'Done'
    ...
    Done
    >>> for i in EmptyList().add(1).add(2).add(3) :
    ...   print i
    ...
    3
    2
    1
    >>> [ i * i for i in EmptyList().add(1).add(2).add(3) ]
    [9, 4, 1]
    """
    return ListIterator(self)

#---

class EmptyList (List) :

  def size (self) :
    return 0

  def isEmpty (self) :
    return True

  def search (self, v) :
    return False

  def elem (self, i) :
    raise IndexOutOfBoundsE()

  def index (self, v) :
    raise NotFoundE()

  def insert(self, i, v) :
    if i == 0 :
        return Node(v,self)
    else :
        raise IndexOutOfBoundsE()

  def remove(self,v) :
    return self

  def append(self,v) :
    return Node(v,self)

  def drop(self,i) :
    if i == 0 :
     return self
    else : 
      raise IndexOutOfBoundsE()

  def __str__ (self) :
    return "[]"

#---

class Node (List) :

  def __init__ (self, head, tail) :
    self.head = head
    self.tail = tail

  def size (self) :
    return 1 + self.tail.size()

  def isEmpty (self) :
    return False

  def search (self, v) :
    return self.head == v or self.tail.search(v)

  def elem (self, i) :
    if i == 0 :
        return self.head
    else :
        return self.tail.elem(i-1)

  def index (self, v) :
    if self.head == v :
        return 0
    else :
        return 1 + self.tail.index(v)

  def insert(self, i, v) :
    if i == 0 :
        return Node(v,self)
    else :
        return Node(self.head,self.tail.insert(i-1,v))

  def remove(self,v) :
    if self.head == v :
        return self.tail
    else :
        return Node(self.head,self.tail.remove(v))

  def append(self,v) :
    return Node(self.head,self.tail.append(v))

  def drop (self,i) : 
   if i == 0 :
       return self
   else :
       return self.tail.drop(i-1)

  def __str__ (self) :
    return "%s, %s" % (self.head, self.tail)

#---

class ListIterator :
  def __init__(self,list) :
    self.list = list

  def next(self) :
    if self.list.isEmpty() :
      raise StopIteration
    else :
      v = self.list.head
      self.list = self.list.tail
      return v

#-----------------------------------------------------------------------------

if __name__ == "__main__" :
  import doctest
  doctest.testmod()
