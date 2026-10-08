"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {None: None} 
        curr = head
        while curr:
            seen[curr] = Node(curr.val) #creates a mapping between the original nodes and the copies
            curr = curr.next 
        curr = head
        while curr: 
            new = seen[curr]
            new.next = seen[curr.next]
            new.random = seen[curr.random]
            curr = curr.next
        return seen[head]
            
            

    #the deepy copy should consist of exactly n new nodes. 
    #while i iterate through the existing linked list, im going to create copies of the nodes in the copied list 
        