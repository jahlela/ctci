
class Node(object):
    
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        """
        >>> new_node = Node(50, 'Lo')
        >>> print new_node
        <__main__.Node | Key: 50, Value: Lo>
        """
        return '<__main__.Node | Key: %s, Value: %s>' %(self.key, self.value)

class DLL(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def enqueue(self, key, value):
        """
        Creates a new node and adds it to the head of DLL, then increments length by 1
        
        >>> dll = DLL()
        >>> dll.enqueue(1, 'Batman')
        <__main__.Node | Key: 1, Value: Batman>
        >>> print dll.head.value
        Batman
        >>> print dll.tail.value
        Batman
        >>> dll.enqueue(2, 'Catwoman')
        <__main__.Node | Key: 2, Value: Catwoman>
        >>> print dll.head.value
        Catwoman
        >>> print dll.tail.value
        Batman

        """
        new_node = Node(key, value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        return new_node

    def dequeue(self):
        """ 
        Removes oldest item from end of DLL and decreases length by 1
        """

        if self.head:
            old_node = self.tail
            
            if self.head is self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

            self.length -= 1
            return old_node
        else:
            raise IndexError("No items found")


        
    def promote(self, node):
        """
        Moves any node already in the DLL to most recently used position
        """
        
        # If node is tail, do nothing
        if node is not self.tail:
            # If node is head (we already know it's not tail):
            # set self.head to self.head.next
            # set self.head.prev = None
            print 'not tail', node
            print node.next # None the first time
            print self.head
            print self.tail
            
            if node is self.head:
                self.head = self.head.next
                try:
                    self.head.prev = None
                except AttributeError:
                    print self.head
                    print 'This should be None'

            else:
                node_to_move = node
                node_before = node_to_move.prev
                node_after = node_to_move.next
                node_before.next = node_after
                node_after.prev = node_before
                
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
class Cache(object):

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = {}
        self.queue = DLL()

    def push(self, key, value):
        """
        >>> cache = Cache()
        >>> cache.push(1, 'Batman')
        >>> cache.push(2, 'Catwoman')
        >>> cache.push(3, 'Hulk')
        >>> cache.push(4, 'Green Lantern')
        >>> cache.push(5, 'Spiderman')
        >>> for item in cache.cache:
        ...    print item
        1
        2
        3
        4
        5
        
        >>> cache.push(6, 'Flash')
        >>> for item in cache.cache:
        ...    print item
        2
        3
        4
        5
        6

        >>>  
        >>>  
        >>>  
        >>>  
        >>>  
        >>>  
        >>>  
        >>>  
        
        """
        if self.queue.length == self.capacity:
            old_node = self.queue.dequeue()
            del self.cache[old_node.key]
            
        new_node = self.queue.enqueue(key, value)
        self.cache[key] = new_node

    def exists(self, key):
        return key in self.cache

    
    def get(self, key):
        """
        >>> cache = Cache()
        >>> cache.push(1, 'Batman')
        >>> cache.push(2, 'Catwoman')
        >>> print cache.get(1)
        Batman

        """

        
        if self.exists(key):
            node = self.cache[key]
            self.queue.promote(node)
            return node.value

        else:
            raise KeyError("Item not found in cache")




if __name__ == "__main__":
    import doctest
    doctest.testmod()
