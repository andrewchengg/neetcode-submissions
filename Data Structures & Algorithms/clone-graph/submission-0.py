"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        hashmap = {} #dictionary where key = is the main node, and the value is the copied node
        seen = set()
        #first we are going to make a copy of all the nodes in the graph
        stack = [] 
        stack.append(node)
        while stack:
            curr = stack.pop()
            if curr not in seen:
                seen.add(curr)
                hashmap[curr] = Node(curr.val) #create the mapping from original to new
                for neighbor in curr.neighbors:
                    stack.append(neighbor)
        for original, copy in hashmap.items():
            for i in original.neighbors:
                copy.neighbors.append(hashmap[i])
        return hashmap[node]
        
            
            
        
                


    #have to remember that whenever we create the dictionary, we have to use the COPY 