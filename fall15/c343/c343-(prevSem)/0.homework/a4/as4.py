#!/usr/bin/python

from math import *

def mHash(k):
  return floor((2**14)*((k*(2654435769.0/(2**32)))%1))

def numCounter(n):
  counts = {} 
  for each in n:
    if each in counts:
      counts[each]+=1
    else:
      counts[each]=1
  return counts.items()

def indexer(n):
  l={}
  i=0
  for each in n:
    each.append(i)
    l.append(each)
    i+=1


nList=[]

for i in range(10**6):
  m=mHash(i)
  nList.append(m)  

counted = numCounter(nList)
  
print indexer(counted)
