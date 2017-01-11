class Node(object):

    def __init__(self, data=None, left=None, right=None):
        """ """
        
        self.data = data
        self.left = left 
        self.right = right

    def __repr__(self):
        return "<__main__.Node object %d>" % (self.data)


    def get_min(self):
        """
        Returns value of smallest node.

        >>> node4.get_min()
        1
        """

        if not self:
            return None

        if self.left is None:
            return self.data
        else:
            return self.left.get_min()

    def get_max(self):
        """
        Returns value of largest node.

        >>> node4.get_max()
        7
        """

        if not self:
            return None

        if self.right is None:
            return self.data
        else:
            return self.right.get_max()


    def is_in_tree(self, value):
        """
        Returns a boolean for whether the value is in the tree.

        >>> node4.is_in_tree(2)
        True
        
        >>> node4.is_in_tree(8)
        False
        """
        
        if self.data == value:
            return True

        if value <= self.data:
            if self.left:
                return self.left.is_in_tree(value)
        else:
            if self.right:
                return self.right.is_in_tree(value)

        return False

    
    def print_in_order(self):
        """
        Prints everything in the tree on a new line from smalles to largest

        >>> node4.print_in_order() 
        1
        2
        3
        4
        5
        6
        7

        """
        if self.left:
            self.left.print_in_order()

        print self.data

        if self.right:
            self.right.print_in_order()

    def get_children(self):
        """ 
        Returns a list of children, if any, that a node has. Does not include None. 

        >>> node4.get_children()
        [<__main__.Node object 2>, <__main__.Node object 6>]

        """
        children = []

        if self.left:
            children.append(self.left)

        if self.right:
            children.append(self.right)

        return children

    def dfs(self, value):
        """ 
        Returns the node with the value or False if not found 
        >>> node4.dfs(2)
        looking for:  2
        checked 4
        checked 6
        checked 7
        checked 5
        <__main__.Node object 2>

        >>> node4.dfs(8)
        looking for:  8
        checked 4
        checked 6
        checked 7
        checked 5
        checked 2
        checked 3
        checked 1
        False

        """
        
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
        """ 
        Returns the node with the value or False if not found 

        >>> node4.bfs(2)
        looking for:  2
        checked 4
        <__main__.Node object 2>

        >>> node4.bfs(8)
        looking for:  8
        checked 4
        checked 2
        checked 6
        checked 1
        checked 3
        checked 5
        checked 7
        False
        
        """
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

            >>> Node.is_valid(node4)
            True

            >>> node6.left = node7
            >>> node6.right = node5
            >>> Node.is_valid(node4)
            False

            Reset to valid tree
            >>> node6.left = node5
            >>> node6.right = node7

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
            # less than our data
            if not ok(node.left, node.data, gt):
                return False

            # general case: check our right child
            # all descendants of right child must be
            # greater than our data 
            if not ok(node.right, lt, node.data):
                return False

            return True

        return ok(self, None, None)

    def is_balanced(self):
        """
        Returns a boolean for whether the tree is balanced
        i.e. the difference between the min leaf depth and the max leaf depth is 1 or less

        >>> node4.is_balanced()
        True

        >>> node18 = Node(18)
        >>> node17 = Node(17, None, node18)
        >>> node16 = Node(16, None, node17)
        >>> node15 = Node(15, None, node16)
        >>> node15.is_balanced()
        False
        """

        depths = []

        nodes = [(self, 0)]

        while len(nodes):
            node, depth = nodes.pop()
            
            if not node.left and not node.right:
                
                if depth not in depths:
                    depths.append(depth)

                    # Check for imbalances
                    if len(depths) > 2:
                        return False
                    if len(depths) == 2 and abs(depths[0] - depths[1]) > 1:
                        return False

            else:
                if node.left:
                    nodes.append((node.left, depth + 1))

                if node.right:
                    nodes.append((node.right, depth + 1))

        return True

                            
node7 = Node(7)
node5 = Node(5)
node6 = Node(6, node5, node7)
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node4 = Node(4, node2, node6)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
