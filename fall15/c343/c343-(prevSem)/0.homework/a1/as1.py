# A web page page is represented as a list consisting of a page number
# followed by the words on the page. 

# Example web pages

p1 = [4,  'the', 'dog', 'chewed', 'the', 'rug']
p2 = [79, 'on', 'the', 'rug', 'slept', 'the', 'dog']
p3 = [32, 'the', 'rug', 'rats', 'slept', 'on']
p4 = [42, 'the', 'meaning', 'of', 'life']

def get_page_number (wp): 
  """Takes a web page and returns its page number.
  >>> get_page_number(p1)
  4
  >>> get_page_number(p2)
  79
  >>> get_page_number(p3)
  32
  >>> get_page_number(p4)
  42
  """
  #print wp[0]
  return wp[0]


def get_words (wp):
  """Takes a web page and returns the list of words on the page.
  >>> get_words(p1)
  ['the', 'dog', 'chewed', 'the', 'rug']
  >>> get_words(p2)
  ['on', 'the', 'rug', 'slept', 'the', 'dog']
  >>> get_words(p3)
  ['the', 'rug', 'rats', 'slept', 'on']
  >>> get_words(p4)
  ['the', 'meaning', 'of', 'life']
  """
  #print wp[1:]
  return wp[1:]


## The World Wide Web is represented as a list of pages. 

www1 = [p1,p2,p3,p4]
www2 = [p3,p1]
www3 = []

def collect_page_numbers (www):
  """Takes a representation of the web as a list of pages and returns
  a list of all the page numbers.
  >>> collect_page_numbers(www1)
  [4, 79, 32, 42]
  >>> collect_page_numbers(www2)
  [32, 4]
  >>> collect_page_numbers(www3)
  []
  """
  pages = []
  for each in www:
      pages.append(each[0])
  #print pages
  return pages 

def occurs (w, ws):
  """Takes a word w and a list of words ws and checks whether w occurs 
  in the list ws.
  >>> occurs('cat',get_words(p1))
  False
  >>> occurs('dog',get_words(p1))
  True
  >>> occurs('chew',get_words(p1))
  False
  >>> occurs('the',get_words(p4))
  True
  """
  which = False
  for word in ws:
      if word == w:
        which = True        
  #print which    
  return which

def remove_duplicates (ws):
  """Takes a list and returns a new list without duplicates.
  >>> remove_duplicates(get_words(p1))
  ['the', 'dog', 'chewed', 'rug']
  >>> remove_duplicates(get_words(p2))
  ['on', 'the', 'rug', 'slept', 'dog']
  >>> remove_duplicates(get_words(p3))
  ['the', 'rug', 'rats', 'slept', 'on']
  >>> remove_duplicates(get_words(p4))
  ['the', 'meaning', 'of', 'life']
  >>> remove_duplicates(['a','b','a','b','a','b','a','b'])
  ['a', 'b']
  """
  ls = []
  for word in ws:
      if word not in ls:
          ls.append(word)
  #print ls      
  return ls

def find_page_numbers (w, www):
  """Takes a word and representation of the web as a list of pages and 
  returns all the pages in which the word occurs.
  >>> find_page_numbers('dog',www1)
  [4, 79]
  >>> find_page_numbers('mouse',www1)
  []
  >>> find_page_numbers('the',www1)
  [4, 79, 32, 42]
  """
  numbers = []
  for each in www:
      if w in get_words(each):
          numbers.append(get_page_number(each))
  #print numbers         
  return numbers
     
def isPrefix (xs, ys) :
  """Takes two lists and returns True if the first list is a prefix of the 
  second and False otherwise:
  >>> isPrefix ([], ['a', 'b', 'c', 'd'])
  True
  >>> isPrefix (['a'], ['a', 'b', 'c', 'd'])
  True
  >>> isPrefix (['a', 'b', 'c'], ['a', 'b', 'c', 'd'])
  True
  >>> isPrefix (['a', 'b', 'c'], ['a', 'b'])
  False
  >>> isPrefix (['a', 'b', 'c'], ['a', 'b', 'x', 'y', 'z'])
  False
  """
  which = True
  if len(xs)>len(ys):
    which = False
  else:
    for i in range(len(xs)):
        if xs[i] != ys[i]:
            which = False
  #print which
  return which

def fuseDNA (seq1, seq2) :
  """DNA is sampled in small fragments, which are then glued together into a
  longer strand. The procedures takes two DNA sequences, seq1 and seq2,
  locates the area of overlap, and returns the result of joining the two
  sequences together. The overlap area is the longest suffix of seq1 that
  matches a prefix of seq2 and it only appears once in the resulting
  sequence:
  >>> fuseDNA(['a','a','a','t','t','t','t'],['t','t','t','t','g','g','g','g'])
  ['a', 'a', 'a', 't', 't', 't', 't', 'g', 'g', 'g', 'g']
  >>> fuseDNA(['a','a','a'],['g','g','g'])
  ['a', 'a', 'a', 'g', 'g', 'g']
  >>> fuseDNA(['a','t','t','a'],['t','t','a','a'])
  ['a', 't', 't', 'a', 'a']
  """
  ls = []
  while (not isPrefix(seq1,seq2)):
      ls.append(seq1[0])
      seq1 = seq1[1:]
  ls += seq2
  return ls

#Uncomment the following to test your code when you finish

if __name__ == '__main__':
  import doctest
  print "Running test cases..."
  doctest.testmod()
