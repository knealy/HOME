
class AVLNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self
        self.height = height(self)

    def after(self):
        node = "something"
        if self.right and self.right.root:
            node = self.right.root
            while node.left and node.left.root:
                node = node.left.root
            return node
        else:
            node = self
            par = self.parent
            while par and (node == par.right.root):
                node = par
                par = node.parent
            return par

    def before(self):
        node = "nope"
        if self.left and self.left.root:
            node = self.left.root
            while node.right and node.right.root:
                node = node.right.root
            return node
        else:
            node = self
            par = node.parent
            while par and (node == par.left.root):
                node = par
                par = node.parent
            return par
    
    def delete(self, n, k, tree):
            # if we find the node
            if self.key == k:
                # and it has two children:
                if self.right.root and self.left.root:
                    # find the successor for the node:
                    replacement = tree.successor(n)
                    # set the current nodes KEY to the successor's key value
                    self.key = replacement.key
                    # if the successor is the node to the right of current,  
                    if self.key == self.right.root.key:
                        self.right.root = None
                        tree.rebal()
                    else:
                        self.left.root = None
                        tree.rebal()
                # if it has one or no children 
                else:
                    if self.left.root:
                        self.key = self.left.root.key
                        self.left.root.key = None
                        
                    else:
                        self.key = self.right.root.key
                        self.right.root.key = None
            else:
                if self.key>k:
                    if self.left.root:
                        self.left.root = self.left.root.delete(n,k,tree)
                        self.left.rebal()
                else:
                    if self.right.root:

                        self.right.root = self.right.root.delete(n,k,tree)
                        self.right.rebal()
            tree.rebal()


    def avl_search(self,k,less):
        if self.key == k:
            return self
        elif less(k, self.key) and self.left.root:
                return self.left.root.avl_search( k, less)
        elif less(self.key, k) and self.right.root:
                return self.right.root.avl_search( k, less)
        else:
            return None

    def __str__(self):
        reply = "["+str(self.key)+", "+str(self.left)+", "+str(self.right)+"]"
        return reply
        
def less_than(x,y):
    return x < y

def height(node):
    if node: 
        return 1 + max(height(node.left), height(node.right))
    else:
        return -1


class AVLTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.less = less
        self.bal = 0
        if self.root:
            self.height = self.root.height
        else:
            self.height = -1

    def rotate_right(self):
        tmp= self.root.left.root
        newleft = tmp.right.root
        org = self.root
        self.root = tmp
        org.left.root = newleft
        tmp.right.root = org

    def rotate_left(self):
        tmp = self.root.right.root
        newleft = tmp.left.root
        org = self.root
        self.root = tmp
        org.right.root = newleft
        tmp.left.root = org

    def new_bal(self,keep="yes"):
        node = self.root
        if node:
            if keep:
                if node.left:
                    node.left.new_bal()
                if node.right:
                    node.right.new_bal()
            self.bal = (node.left.height - node.right.height)
        else:
            self.bal = 0

    def new_height(self, keep="yes"):
        node = self.root
        if node:
            if keep:
                if node.left:
                    node.left.new_height()
                if node.right:
                    node.right.new_height()
            self.height = 1+max(node.left.height, node.right.height)
        else:
            self.height = -1

    def rebal(self):
        self.new_height(None)
        self.new_bal(None)
        while (self.bal > 1) or (self.bal < -1):
            if self.bal < -1:
                if self.root.right.bal > 0:
                    self.root.right.rotate_right()
                    self.new_height()
                    self.new_bal()
                self.rotate_left()
                self.new_height()
                self.new_bal()
            if self.bal >1:
                if self.root.left.bal < 0:
                    self.root.left.rotate_left()
                    self.new_height()
                    self.new_bal()
                self.rotate_right()
                self.new_height()
                self.new_bal()

    # takes value, returns node with key value
    def insert(self, k):
        newNode = AVLNode(k)
        if not self.root:
            self.root = newNode
            self.root.left = AVLTree()
            self.root.right = AVLTree()
        elif k > self.root.key:
            self.root.right.insert(k)
        else:
            self.root.left.insert(k)
        self.rebal()
        return newNode

    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):
        return n.after()

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        return n.before()

    # takes key returns node
    # can return None
    def search(self, k):
        if self.root:
            return self.root.avl_search(k, self.less)
        else:
            return self.root

    def delete_node(self, n):
        if self.root:
            self.root.delete(n, n.key, self)

    def __str__(self):
        return str(self.root)


def main():
    a1 = AVLTree()
    # insert tests
    # a1.insert(1)
    # print a1
    # a1.insert(2)
    # print a1
    # a1.insert(3)
    # print a1
    # a1.insert(4)
    # print a1
    # a1.insert(2)
    # print a1

    assert a1.height == -1
    assert a1.insert(6).key == 6
    # print a1
    assert a1.height == 0
    assert a1.bal == 0
    assert a1.insert(9).key == 9
    # print a1
    assert a1.insert(2).key == 2
    # print a1
    assert a1.height ==1 
    assert a1.bal == 0
    assert a1.insert(10).key == 10
    # print a1
    assert a1.insert(11).key == 11
    assert a1.bal == -1 
    # print a1
    assert a1.bal == -1
    assert a1.insert(12).key == 12
    print a1
    
    # search tests
    assert a1.search(9).key == 9
    # print a1.search(9)
    assert a1.search(6).key != 2
    assert a1.search(6).key == 6
    assert a1.search(7) == None
    # print a1.search(7)

    # rotate right test
    # print a1
    # a1.rotate_right()
    # print a1
    # a1.rotate_right()
    # print a1

    # #rotate left test
    # a1.rotate_left()
    # print a1
    # a1.rotate_left()
    # # print a1

    # # # deletion tests
    # 1 child
    a1.delete_node(a1.root.right.root)
    print a1
    # a1.delete_node(a1.root.right.root)
    # print a1
    # a1.delete_node(a1.root.left.root)
    # print a1

    # print a1.height
    # print a1.bal
    # # 0 children
    # print a1.bal
    # # # 2 children 
   

if __name__ == "__main__":
    main()