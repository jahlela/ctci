class Node(object):

    def __INIT__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left 
        self.right = right

    def get_children(self):
        """ Returns a list of children, if any, that a node has. Does not include None. """
        children = []

        if self.left:
            children.append(self.left)

        if self.right:
            children.append(self.right)

        return children


    def insert(self, value):
        if value <= self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)


    def find(self, value):
        if self.data == value:
            return True

        if value <= self.data:
            if self.left:
                return self.left.find(value)
        else:
            if self.right:
                return self.right.find(value)

        return False

    
    def print_in_order(self):
        if self.left:
            self.left.print_in_order()

        print self.data

        if self.right:
            self.right.print_in_order()

            
    def dfs(self, value):
        """ Returns the node with the value or False if not found """
        print 'looking for: ', value
        to_visit = [self]

        while to_visit:
            node = to_visit.pop()

            if node.data == value:
                return node
            else:
                print 'checked', node.data
                to_visit += node.get_children()

        return False

    def bfs(self, value):
        """ Returns the node with the value or False if not found """
        print 'looking for: ', value
        to_visit = [self]

        while to_visit:
            cur = to_visit.pop(0)

            if cur.data == value:
                return cur
            else:
                print 'checked', cur.data
                to_visit += cur.get_children()

        return False


    def is_valid(self):

        def ok(node, lt, gt):
            """
            Check this node & recurse to children
            
            lt: left children must be <= this
            gt: right child must be >= this
            """

            # base case: this isn't a node
            if not node:
                 return True

            # base case: smaller than allowed
            if lt is not None and node.data > lt:
                 return False

            # base case: bigger than allowed
            if gt is not None and node.data < gt:
                return False

            # general case: check our left child
            # all descendants of left child must be
            # less than our data (and greater than
            # whatever we had to be greater than).
            # if not, fail fast.
            if not ok(node.left, node.data, gt ):
                return False


            # general case: check our right child
            # all descendants of right child must be
            # greater than our data (and less than
            # whatever we had to be less than)
            # if not, fail fast.
            if not ok(node.right, lt, node.data):
                return False

            return True

        return ok(self, None, None)

class TNode(object):
    def __INIT__(self, cat, fish, monk):
        self.left = cat
        self.right = fish
        self.data = monk


node7 = Node(7)
node5 = Node(5)
node6 = Node(6, node5, node7)
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node4 = Node(4, node2, node6)

print '\nnode4.find(2)', node4.find(2)
print '\nnode4.find(8)', node4.find(8)
print '\nnode4.print_in_order()', node4.print_in_order()
print '\nnode4.dfs(2)', node4.dfs(2)
print '\nnode4.bfs(2)', node4.bfs(2)
print '\nvalid:', Node.is_valid(node4)



    
