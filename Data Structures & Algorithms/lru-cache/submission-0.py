class Node: 
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left 
    
    def _remove(self, node): 
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node 

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)                                 # move to most-recent end
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])                  # drop the old position
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.cap:
            lru = self.left.next                           # least recent = right after the left dummy
            self._remove(lru)
            del self.cache[lru.key]    

        

        
