# Overview:

# Heaps continued:
# 	- increase key
# 	- insert
# Greedy algorithms:
# 	- activity selection
# 	- Huffman codes

# increase key to 20...
# (drawing)

# max_heapify = bubble things down, 
# now lets bubble them up

# as soon as you know node is > than parent, swap, it will automatically be greater than children

# heap_insert
# (drawing)..

# ---------------------------------------------------------------------------------
# Greedy algorithms:

# activity selection problem:
# 	- lots of event requests for the same venue, different length events tht pay the same. 
# 	- How should we schedule them algorithmically?

# schedule weddings, 1 hall
# wedding request: start-time, finish-time
# same $ per wedding

#     0  1  2  3  4 
# s: 1  2  
# f: 3  4

# 0                                                        20
# |-----------------------------|
#   |-r5-| |--r7--|  |-r2-|  |--r10--|
 
#  			(recursion)
#  |~~~~~~~|-r1-|~~~~~~~~~~~~~~~~|   choice 0
#  vs. 			(recursion)
#  |~~~~|-r2-|~~~~~~~~~~~~~~~~~~~|   choice 1

# more effecient to choose the events with the earliest finish-time

# |-------------------------------|
#    |---|
#  |-----|
#    |--|
#          |---|

# Greedy algorithm approach actually gives optimal solutions for this problem structure. 

# Proof:
# - Suppose we have an optimal solution A, for a set of activities.
# - Let A' be the activity with earliest finish-time
# case a' in A:
	# look at A - {a'}, use induction hypothesis 
# case a' not in A:
	# A' = A - {a} U {a'}
# a is 1st to finish in A


# Huffman Codes:

	# Have some long sequence of dna:
	# CTCT	CTCT	AGCT	AGCC	AGCC	TGAA ...

# Concept 1: use smaller codes for high freq. words. 

# CTCT: 4
# CATC: 3
# AGCC: 2
# AGCT: 1
# TGAA: 1

# Concept 2: make sure that no code is a prefix of another.

# Correct:
# 01 
# 111
# 101

# Wrong:
# 01
# 011
# 0110

# prefix nature prevents ambiguity between words
# 01111101111
#  01 
#     111 
#          101 
#               111

# (drawing)...

