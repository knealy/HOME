from stack import ArrayStack

class BSTNode:
    def __init__(self, key, left=None, right=None,parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self 

    def delete(self, n, k, tree):
        # if we find the node
        if self.key == k:
            # and it has two children:
            if self.right and self.left:
                replacement = tree.successor(n)
                self.key = replacement.key
                if self.key == self.right.key:
                    self.right = None
                    return self
                else:
                    self.left = None
                    return self
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if self.key>k:
                if self.left:
                    self.left = self.left.delete(n,k,tree)
            else:
                if self.right:
                    self.right = self.right.delete(n,k,tree)
            return self

    def __str__(self):
        reply = "["+str(self.key)+", "+str(self.left)+", "+str(self.right)+"]"
        return reply

def less_than(x,y):
    return x < y

class BinarySearchTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.parents = True
        self.less = less

    # takes value, returns node with key value
    def insert(self, k):
        newNode = BSTNode(k)
        if self.root:
            node = self.root
            while node:
                if self.less(node.key,k):
                    if node.right:
                        node = node.right
                        continue
                    else:
                        node.right = newNode
                        break
                else:
                    if node.left:
                        node = node.left
                        continue
                    else:
                        node.left = newNode
                        break
            newNode.parent = node
        else:
            self.root = newNode
        return newNode

    # return the node with the smallest key greater than n.key
    def successor(self, n):
        node = "nope"
        if n.right:
            node = n.right
            while node.left:
                node = node.left
            return node
        else:
            node = n
            par = node.parent
            if par:
                if par.right == node:
                    node = par
                    par = node.parent
                return par
        
    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        node = "nope"
        if n.left:
            node = n.left
            while node.right:
                node = node.right
            return node
        else:
            node = n
            par = node.parent
            if par:
                if (node == par.left):
                    node = par
                    par = node.parent
                return par


    # takes key returns node
    # can return None
    def search(self, k):
        node = self.root
        while node:
            if self.less(k,node.key):
                node = node.left
            elif self.less(node.key,k):
                node = node.right
            else:
                break
        return node

    # takes node, deletes it from the tree if it exists
    def delete_node(self, n):
        if self.root:
            self.root = self.root.delete(n, n.key,self)
            return self.root
 
    def __str__(self):
        return str(self.root)

def main():
    #r = BSTNode(5,BSTNode(2),BSTNode(8))
    t1 = BinarySearchTree()
    print t1
    assert t1.insert(6).key == 6
    print t1
    # assert t1.insert(1).key == 1

    # assert t1.successor(t1.root).key == 6

    # assert t1.predecessor(t1.root.left).key == 1
    # t1.insert(3)

    # # delete_node removes the node from tree and returns the root of mutated tree
    # #case for 1 child
    # assert t1.root.right.key == 8
    # t1.delete_node(t1.root.right)
    # assert t1.root.right.key == 6
    # # case for no children
    # t1.delete_node(t1.root.right)
    # assert t1.root.right == None
    # # case for 2 children
    # assert t1.root.left.key == 2
    # t1.delete_node(t1.root.left)
    # assert t1.root.left.key == 3
    # assert t1.root.key == 5
    # assert t1.root.left.key == 3
    # assert t1.root.right == None
    # assert t1.root.left.right == None
    # assert t1.root.left.left.key == 1
    # assert (t1.root.left.left.left == None) and (t1.root.left.left.right == None)

if __name__ == '__main__':
    main()

