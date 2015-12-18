
# Overview:

# Heaps & Priority Queues:

# - unix_heapify
# - build_max_heap
# - heap_maximum
# - heap_insert
# - heap_extract_max
# - heap_increase_key
# - heap_sort

# Motivations:
# - need a set with first access to element with largest key
# - In-place Sorting
# - Change key of element in set

# Main thought - priority queue (bribe most = served first)
# prioritized way of handling elements of a set.

# ---------------------------------------------------
#def: 
#A max heap is a heap where every node except root satisifies: 
# H[i] <= H[parent(i)]

# max_heapify turns a non max heaped tree (or subtree) into a max heap
# implement max_heapify:

def unoptimal_max_heapify(H, i, n):
	if right(i) < n:
		if H[left(i)] > H[right(i)]:
			larger = left(i)
		else:
			larger = right(i)
		swap(H,larger,i)

def max_heapify(H,i,n):
	# if left child exists and is > than H[i]
	if left(i) < n and H[i] < H[left(i)]:
		# largest = left child index
		largest = left(i)
	else: 
		# largest = current index
		largest = i
	# if the right child exist and is bigger than largest element 
	if right(i) < n and H[largest] < H[right(i)]:
		# set largest to right child index
		largest = right(i)
	# if current index is not largest:
	if largest != i:
		# switch current element with largest
		swap(H, i, largest)
		# recursion with index of largest element
		max_heapify(H,largest,n)

# time complexity?
# Worst case - prob node is root and must percolate down the tree to bottom.
# O(log n) with n=height of tree

def build_max_heap(H):
	last_parent = (len(H)/2)-1
	for i in range(last_parent,-1,-1):
		max_heapify(H,i)
# time complexity?
# O(n lg n)
# how many nodes are there at each height of tree?
# at height 0 = n/2
# at height 1 = n/4
# at height 2 = n/8

# sum_series(n,lg n, h=0) (h/2^n)

def keep_maximum:
	return h[0]

def heap_sort(H):
	build_max_heap(H)	# O(n)
	n = len(H)
	# swap the keep_maximum of heap with the last element
	# call max_heapify on the new root/beginning of heap
	for i in range(len(H)-1, 0, -1):	  # O(n lg n)
		swap(H, 0, i)
		n =n-1
		max_heapify(H,0, n)	# O(lg n)

# time complexity:
# O(n lg n) + O(n)