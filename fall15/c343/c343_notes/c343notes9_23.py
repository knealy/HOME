# notes 9/23

class BSTnode:
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = None

	def search(self,k,less):
		if self.key == k:
			return self
		elif less(k,self.key):
			if self.left:
				return self.left.search(k,less)
			else:
				return None
		else:
			if self.right:
				return self.right.search(k,less)
			else:
				return None



r = BSTnode(5,BSTnode(2),BSTnode(8))


# Visual rep of BSTNodes:

# 		5
# 	2 		8
# None	   None	    None  None

# BST

def less_than(x,y):
	return (x<y)

def gtr(x,y):
	return (x>y)		

# Higher-order programming in languages (functions + classes = fun stuff)
# possibility to order the trees differently
#T = BinarySearchTree(r,gtr)

# binary search tree is mainly about bundling the trees and the comparison function together

class BinarySearchTree:
	def __init__(self,root=None,less=less_than):
		self.root = root
		self.less = less_than

# Visual rep of BSTNodes:

# 	         r=5 <----------- T = (root,less)
# 	2 		8
# None	   None	    None  None

	# search needs a recursive function that cannot be itself because its in BST class but working on BSTNode class
	# so add a method to BSTnode class that it can interact with. ^^
	def search(self,k):
		if self.root:
			return self.root.search(k,self.less)
		else:
			return None

	def searchN(self,k):
		node = self.root
		while node:
			if self.less(k, node.key):
				node = node.left
			elif self.less(node.key,k):
				node = node.right
			else:
				break
		return node


def search_for(k,node,less):
	current = node
	while current:
		if less(k,current.key):
			current = current.left
		elif less(current.key,k):
			current = current.right
		else:
			break
	return current


T = BinarySearchTree(r)

# all 3 forms of the function pass same test
assert T.search(8).key==8
assert T.searchN(8).key==8
assert search_for(8,T.root,less_than).key==8

# node is heavier if it is taller

# something about AVIs ...

# From changed node on up:
# 	update the heights
# 	move up to the lowest node x thats not in AVL
# 	k+2
# k-1		k+1  <-- x.right
# 	[]		[]

# delete (harder for unbalanced trees)

# 1. if x.right	right heavy
# 		x
# 	a 		y
# 		b 		c 


# 2. x.right is balanced.

# ?? lost me !
