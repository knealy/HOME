Lecture: Code for BSTs, cont'd balanced trees (AVL)
===================================================

* review code for BSTs

    class BSTNode:
	def __init__(self, key, left=None, right=None):
	    self.key = key
	    self.left = left
	    self.right = right
	    self.parent = None

    def less_than(x,y):
	return x < y

    class BinarySearchTree:
	def __init__(self, root = None, less=less_than):
	    self.root = root
	    self.less = less

	def search(self, k):
	    if self.root:
		return self.search_node(self.root, k)
	    else:
		return None

	def search_node(self, node, k):
	    if self.less(k, node.key):
		if node.left:
		    return self.search_node(node.left, k)
		else:
		    return None
	    elif self.less(node.key, k):
		if node.right:
		    return self.search_node(node.right, k)
		else:
		    return None
	    else:
		return node

    if __name__ == "__main__":
	r = BSTNode(5, BSTNode(2), BSTNode(8))
	T = BinarySearchTree(r)
	assert T.search(8).key == 8
	assert T.search(3) == None

*** student work: 
  change search_node to be a method on BSTNode
  change search_node to be a procedure (not a method of any class)


* AVL cont'd, recall the tree rotations:

           y                  x
          / \    right(y)    / \
         x   C  -------->   A   y
        / \     <--------      / \
       A   B     left(x)      B   C

    * Algorithm for fixing AVL property

      From the changed node on up  (there can be several AVL violations)
         - update the heights
         - suppose x is the lowest node that is not AVL
         - wlog. assume x.right is higher than x.left
           1. if x.right is right-heavy,

                  x k+2                              y k+1
                 / \          left_rotate(x)        / \
            k-1 A   y k+1     ===============>   k x   C k
                   / \                            / \
              k-1 B   C k                  k-1 A   B k-1

           2. if x.right is balanced,

                  x k+2                              y k+2
                 / \          left_rotate(x)        / \
            k-1 A   y k+1     ===============> k+1 x   C k
                   / \                            / \
                k B   C k                    k-1 A   B k
         
          3. if x.right is left-heavy

               k+2 x                               y k+1
                  / \                            /   \
             k-1 A   z k+1    RR(z), LR(x)    k x     z k
                    / \      =============>    / \   / \
                 k y   D k-1              k-1 A   B C   D k-1
                  / \
                 B   C  k-1 or k-2

    **** Student group work: Given the following AVL Tree, 
       delete the node with key 8 and restore the AVL property
       using tree rotations as described above.
       (This example has two nodes that end up violating the AVL property.)

                 8
               /   \
              5     10
             / \   / \
            2   6 9   11
           / \   \      \
          1   3   7      12
               \
                4

    Solution: 
       * Step 1: replace node 8 with node 9
                 9
               /   \
              5     10
             / \     \
            2   6     11
           / \   \      \
          1   3   7      12
               \
                4

      * Step 2: find lowest node that breaks the AVL property: node 10
      * Step 3: rotate 10 left
                 9
               /   \
              5      11
             / \    /  \
            2   6  10   12
           / \   \       
          1   3   7       
               \
                4

      * Step 4: find lowest node that breaks the AVL property: node 9
      * Step 5: rotate 9 right
                5
             /     \
            2        9
           / \     /   \
          1   3   6     11    
               \   \   /  \
                4   7 10   12


    * AVL Sort
      - insert n items: O(n lg n)
      - in-order traversal: O(n)
      - overall time complexity: O(n lg n)

    * ADT's
      - priority queue
        insert, delete, min
      - ordered set
        insert, delete, min, max, after, before
