"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
"""
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        
        if slow is fast:
            return True
        
    return False

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3

print has_cycle(node1)

node4.next = None

print has_cycle(node1)

""" 1 -> 2 -> 3 -> 4 -> 3 """
