
# Lec. 2: Lists; functions; doctest

def middle (n) : 
  """Takes a positive 3 digit number and returns the digit in the middle:
  >>> middle (123)
  2
  >>> middle (243)
  4
  """
  return (n / 10) % 10

def evens (xs) : 
  """Takes a list of numbers and returns a new list with just the even numbers:
  >>> evens ([])
  []
  >>> evens ([1,2,3,4])
  [2, 4]
  >>> evens ([3,3,3,5,9,1])
  []
  >>> evens ([2,2,2,2,2])
  [2, 2, 2, 2, 2]
  >>> evens ([1,2,3,4]) == [2,4]
  True
  """
  result = []
  for x in xs :
    if x % 2 == 0 :
      result.append(x)
  return result

def evens1 (xs) : 
  """Takes a list of numbers and returns a new list with just the even numbers:
  >>> evens1 ([])
  []
  >>> evens1 ([1,2,3,4])
  [2, 4]
  >>> evens1 ([3,3,3,5,9,1])
  []
  >>> evens1 ([2,2,2,2,2])
  [2, 2, 2, 2, 2]
  >>> evens1 ([1,2,3,4]) == [2,4]
  True
  """
  return filter (lambda n : n % 2 == 0 , xs)
#
#  def f (n) : return n % 2 == 0
#  return filter (f,xs)
#

def evens2 (xs) : 
  """Takes a list of numbers and returns a new list with just the even numbers:
  >>> evens2 ([])
  []
  >>> evens2 ([1,2,3,4])
  [2, 4]
  >>> evens2 ([3,3,3,5,9,1])
  []
  >>> evens2 ([2,2,2,2,2])
  [2, 2, 2, 2, 2]
  >>> evens2 ([1,2,3,4]) == [2,4]
  True
  """
  return [ x for x in xs if x % 2 == 0 ]

def prod (xs) : 
  """Takes a list of numbers and returns the product:
  >>> prod (range(6))
  0
  >>> prod ([])
  1
  >>> prod ([1,2,3,4])
  24
  >>> prod ([4])
  4
  """
  result = 1
  for x in xs :
    result = result * x
  return result  

def prod1 (xs) : 
  """Takes a list of numbers and returns the product:
  >>> prod1 (range(6))
  0
  >>> prod1 ([])
  1
  >>> prod1 ([1,2,3,4])
  24
  >>> prod1 ([4])
  4
  """
  return reduce (lambda a , b : a * b , xs, 1)

def fib (n) : 
  if n < 2 :
    return n
  else :
    return fib (n-1) + fib (n-2)


if __name__ == "__main__" :
  import doctest
  doctest.testmod()
