# Dynamic programming...

import sys
import math
from random import *

#-----------------------------------------------------------------------------
# Warm-up: Fibonacci

# Inefficient fib

def fibR (n) :
    if n < 2 :
        result = n
    else :
        result = fibR (n-1) + fibR (n-2)
    return result

# Top down memoized

class Fib_Memo :
    def __init__ (self) :
        self.memo = {}    

    def calc (self,n) :
        if n in self.memo :
            return self.memo[n]
        
        if n < 2 :
            result = n
        else :
            result = self.calc(n-1) + self.calc(n-2)

        self.memo[n] = result
        return result

# Bottom up

class Fib_BU :
    def __init__ (self) :
        self.results = {}

    def calc (self,n) :
        self.results[0] = 0
        self.results[1] = 1
        for i in range(2,n+1) :
            self.results[i] = self.results[i-1] + self.results[i-2]
        return self.results[n]
    
#-----------------------------------------------------------------------------
# Longest common subsequence

short_strand1 = 'ABCBDAB'
short_strand2 = 'BDCABA'

strand1 = 'ACCGGTCGAGTGCGCGGAAGCCCGGCCGAA'
strand2 = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'

def lcs (seq1,seq2) :
    i = len(seq1)
    j = len(seq2)
    if i == 0 or j == 0 :
        r = ''
    elif seq1[i-1] == seq2[j-1] :
        r = lcs(seq1[:i-1],seq2[:j-1]) + seq1[i-1]
    else :
        r1 = lcs(seq1[:i-1],seq2)
        r2 = lcs(seq1,seq2[:j-1])
        if len(r1) > len(r2) :
            r = r1
        else :
            r = r2
    return r

class LCS :
    def __init__ (self) :
        self.memo = {}

    def lcs (self,seq1,seq2) :
        
        if (seq1,seq2) in self.memo :
            return self.memo[(seq1,seq2)]

        i = len(seq1)
        j = len(seq2)
        if i == 0 or j == 0 :
            r = ''
        elif seq1[i-1] == seq2[j-1] :
            r = self.lcs(seq1[:i-1],seq2[:j-1]) + seq1[i-1]
        else :
            r1 = self.lcs(seq1[:i-1],seq2)
            r2 = self.lcs(seq1,seq2[:j-1])
            if len(r1) > len(r2) :
                r = r1
            else :
                r = r2

        self.memo[(seq1,seq2)] = r
        return r

