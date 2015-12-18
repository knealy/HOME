# Programming = data + operations
# Ease and efficiency of writing operations depends on how data is represented
# 
# Basic Python data structures
# list, string, tuple, set, dictionary
# Mutable vs immutable (persistent) data structures

# run the following if file loaded as script

if __name__ == "__main__":

  # list
  # collection of things
  # mutable

  xs = ['a', 'b', 'd', 'd', 'e']
  print xs
  xs.append('f')
  print xs
  xs.extend(['g', 'h', 'i'])
  print xs
  xs.insert(2, 'c')
  print xs
  xs.remove('d')
  print xs
  print xs.pop()
  print xs
  print xs.pop(0)
  print xs
  print xs.index('d')
  xs.extend(['h','h','h'])
  print xs.count('h')
  xs.reverse()
  print xs
  xs.sort()
  print xs
  del xs[1]
  print xs

  # now we want to get a feeling the efficiency of these operations

  from timeit import timeit

  # explain side effect of testing

  def appending (s):
    xs = range (s)
    def f (): xs.append(0)
    print 'Appending one million elements to a list of size %d takes %f s' % \
            (s , timeit(f,number=1000000))

  appending(1000)
  appending(2000)
  appending(4000)
  appending(8000)

  def inserting (s):
    xs = range (s)
    def f (): xs.insert(0,0)
    print 'Inserting one million elements in a list of size %d takes %f s' % \
            (s , timeit(f,number=1000000))
  inserting(1000)
  inserting(2000)
  inserting(4000)
  inserting(8000)

  from collections import deque

  ys = deque (['a', 'b', 'd', 'd', 'e'])
  print ys
  ys.append('f')
  print ys
  ys.appendleft('a')
  print ys

  def appendingQ (s):
    xs = deque(range (s))
    def f (): xs.append(0)
    print 'Appending one million elements to a dequeue of size %d takes %f s' \
      % (s , timeit(f,number=1000000))
  appendingQ(1000)
  appendingQ(2000)
  appendingQ(4000)
  appendingQ(8000)

  def insertingQ (s):
    xs = deque(range (s))
    def f (): xs.appendleft(0)
    print 'Inserting one million elements in a dequeue of size %d takes %f s' \
      % (s , timeit(f,number=1000000))
  insertingQ(1000)
  insertingQ(2000)
  insertingQ(4000)
  insertingQ(8000)
