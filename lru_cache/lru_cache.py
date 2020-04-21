from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.cache:
            return None
        else:
            node = self.cache[key]
            self.storage.move_to_end(node)

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.cache:  # If key exists in the cache
            node = self.cache[key]  # grab it and assign it to a node
            node.key = key   # Extract the key and value passed into function call and assign to node
            node.value = value
            self.storage.move_to_end(node)  # assign the node to the front
        if self.size == self.limit:  # If we've hit the limit in the Cache...
            self.storage.remove_from_tail()  # Remove the LRU item in the list 
        if key in self.cache is True:  # if the key already exists in the cache...
            self.value = node.value   # Reassign the value with the new value 
  
        




