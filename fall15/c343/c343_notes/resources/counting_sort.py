
def count_sort(A,B,K):
	# step 0
	c = [0 for i in range(0, k+1)]	 # O(k)
	# step i-1                                 # O(n)
	for i in A:
		c[i]+=1
	# step 2
	for i in range(1,len(c)):             # O(k)
		c[i] = c[i-1]+c[i]
	# step 3
	for j in reversed(A):                  # O(n)
		B[c[j]-1]=j
		c[j]-=1

# Total time complexity: O(n + k)


def radix_sort(A,d):
	B = [0 for i in A]
	for i in range(0,d):
		count_sort(A,B,9,digit(i))	# O(n)
		A[:]=  B[:]

def bucket_sort(A):
	# arr of buckets
	B = [[] for i in A]	# O(n)
	for i in A:		# O(n)
		B[int(i*len(A))].append(i)
	for buck in B:		# O(n)
		buck.sort()
	ret = []
	for buck in B:		# O(n)
		ret+=buck
	return ret
