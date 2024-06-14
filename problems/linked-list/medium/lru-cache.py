# Ok even Neet uses tail + head dummy nodes, for double linked list
# Neet also uses the private subroutines
# 41% runtime, 61% memory
# Yea simpler solution, just two helper functions without worrying about memory cleanup
class Node_V3(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache_Neet(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.tail = Node_V3()
        self.head = Node_V3()
        self.tail.next = self.head
        self.head.prev = self.tail
        self.key_to_node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_node:
            self._remove(self.key_to_node[key])
        node = Node_V3(key, value)
        self._add(node)
        if len(self.key_to_node) > self.capacity:
            self._remove(self.tail.next)

    def _add(self, node):
        self.key_to_node[node.key] = node
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.key_to_node[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 45% runtime, 69% memory
# Sigh this question was a complete disaster, took 2 hrs and looking at one Python solution
# Ok here it what helps
#   Write class helper functions
#   You need both prev + next pointers 
#   prev + next pointers -> use Two Dummy Nodes (both initially connected to each other) 
#   'get' mutates the list, which is unintuitive because 'get' is meant to be a read-only method
# This is definitely a hard to implement - quite a few edge cases, needing 50+ LOCs
# I had most of the intuition down in first 10 minutes, but struggled to implement it correctly

class Node_V3(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache_V3(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.tail = Node_V3()
        self.head = Node_V3()
        self.tail.next = self.head
        self.head.prev = self.tail
        self.key_to_node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._orphanNode(node)
        self._addNode(node)
        return node.val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_node:
            self._deleteNode(self.key_to_node[key])

        node = Node_V3(key, value)
        self._addNode(node)
        if len(self.key_to_node) > self.capacity:
            self._deleteNode(self.tail.next)

    def _deleteNode(self, node):
        node = self._orphanNode(node)
        del self.key_to_node[node.key]
        del node

    def _orphanNode(self, node):
        # Remove from LL
        node.prev.next = node.next
        node.next.prev = node.prev
        # Update node pointers
        node.prev = None
        node.next = None
        return node

    def _addNode(self, node):
        # node links
        node.prev = self.head.prev
        node.next = self.head
        # head links
        self.head.prev.next = node
        self.head.prev = node
        # global state
        self.key_to_node[node.key] = node
        return node


class Node_V2(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache_v2(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.key_to_node = {}
        self.tail = Node_V2()
        self.head = self.tail
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_to_node:
            node = self.key_to_node[key]
            if node.next:
                # Remove from list
                node.prev.next = node.next
                node.next.prev = node.prev
                # Insert at head
                node.next = None
                self.head.next = node
                node.prev = self.head
                self.head = node
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_node:
            new_node = self.key_to_node[key]
            new_node.val = value
            # If not head, need to remove
            if new_node.next:
                new_node.prev.next = new_node.next
                new_node.next.prev = new_node.prev
                new_node.next = None
        else:
            new_node = Node_V2(key, value)
            self.key_to_node[key] = new_node
            self.size += 1
        
        self.head.next = new_node
        new_node.prev = self.head
        self.head = new_node

        if self.size > self.capacity:
            node_to_remove = self.tail.next
            self.tail.next = node_to_remove.next
            self.tail.next.prev = self.tail
            del self.key_to_node[node_to_remove.key]
            self.size -= 1

# O(1) time average for 'get' and 'put'?
# set 'capacity'
# 'get' returns -1 if not present, else returns value
# 'put' - Update value of key if key exists, otherwise add key-value to the cache. Evict least recently used key
# key and value both >= 0

# Back of LinkedList -> tail, maintain ptr to this
# Maintain size
# Maintain map of key -> Node
# Least recently used key...

# Sigh I hope this doesn't require a double-headed LinkedList Node, 56 minutes in and got tripped up by single node edge case
class Node(object):
    def __init__(self, key = None, val=0, prev = None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.key_to_node = {}
        self.tail = Node()
        self.head = self.tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_to_node:
            ptr = self.key_to_node[key]

            # Remove from current place
            ptr.prev.next = ptr.next
            if ptr.next: ptr.next.prev = ptr.prev

            # Becomes new head
            self.head.next = ptr
            ptr.prev = self.head
            self.head = ptr
            
            return ptr.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_node:
            ptr = self.key_to_node[key]
            ptr.val = value
            ptr.prev.next = ptr.next
            if ptr.next: ptr.next.prev = ptr.prev
            ptr.next = None
        else:
            ptr = Node(key, value)
            self.key_to_node[key] = ptr
            self.size += 1
        
        self.head.next = ptr
        ptr.prev = self.head
        self.head = ptr

        # Remove from tail
        if self.size > self.capacity:
            # Remove node next to tail
            node_to_remove = self.tail.next
            self.tail.next = node_to_remove.next
            self.tail.next.prev = self.tail
            del self.key_to_node[node_to_remove.key]
            self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)