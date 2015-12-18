
# Lec. 3: Big-O

def fibE (n) : 
  if n < 2 :
    return n
  else :
    return fibE (n-1) + fibE (n-2)

def fibL (n) : 
  def helper (i,p,pp) :
    if i == n : 
      return p + pp
    else :
      return helper(i+1,p+pp,p)
  if n < 2 : 
    return n
  else :
    return helper(2,1,0)

if __name__ == "__main__" :

  from timeit import timeit

  # map(fibE,range(17))
  # map(fibL,range(17))

  def fibT (n) : 
    print 'fibE(%d) takes %d seconds' % \
      (n, timeit(lambda : fibE(n),number=1))
    print 'fibL(%d) takes %d seconds' % \
      (n, timeit(lambda : fibL(n),number=1))

  # fibT(10)
  # fibT(20)
  # fibT(30)
  # fibT(35)
  # fibT(36)
  # fibT(37)
  # fibT(38)
  # fibT(39)
  # fibT(40)
  # ...


