def union(A,B):
	#Algorithm for representing the union of two sorted sequences should do the following:
	#1. create a list (array) and counter (integer) for iterating over the list.
	r = []
	cnt = -1

	#2. Create index variables  to iterate over the given sequences.
	a = 0
	b = 0

	#3. Iterate over each sequence until we reach the end of both.
	while a < len(A) and b < len(B):
		if r:
			if a < len(A) and r[-1] == A[a]:
				a+=1
	            		continue
	        		if b < len(B) and r[-1] == B[b]:
	            		b+=1
	           		continue
	           # when a runs out of items, just insert B:
	           if a >= len(A):
	           	r.append(B[b])
	           elif b >= len(B):
	           	r.append(A[a])
	    	elif A[a] < B[b]:
	        		r.append(A[a])
	    	else:
	        		r.append(B[b])
		return r

l1 = [1,2,3,4,5,7,9]
l2 = [3,6,8,11]

R = union(l1,l2)
print R