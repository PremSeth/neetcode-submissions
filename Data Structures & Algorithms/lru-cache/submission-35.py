class Node: 
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity 
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.next = self.right
        self.right.prev = self.left
        self.num = 0

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.next=self.right
        node.prev = prev
        self.right.prev = node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if self.num < self.cap:
                new = Node(key, value)
                new.key = key
                self.cache[key] = new
                self.insert(new)
                self.num +=1
            else:
                self.cache.pop(self.left.next.key)
                self.remove(self.left.next)
                node = Node(key, value)
                node.key = key
                self.insert(node)
                self.cache[key] = node
