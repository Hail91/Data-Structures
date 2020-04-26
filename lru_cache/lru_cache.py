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
        if key not in self.cache:  # If they key is not in the hashtable, return None
            return None
        else: # Otherwise..
            node = self.cache[key]   # Assign the value of item at the cache @ position [key] to node variable.
            self.storage.move_to_front(node) # Assign that node to the most recently used item (Front)
            return node.value[1] # Return the value of the node, which is a tuple containing a key and value, value is located at position '1' of the tuple

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
            node = self.cache[key]  # grab it's value and assign it to a node
            node.value = (key, value) # Assign key and value passed into set method to the nodes value as a tuple
            self.storage.move_to_front(node) # Move the node to the front of the DLL
            return node # Return it out which will terminate the function at this point.
        if self.size == self.limit:  # If we've hit the limit in the Cache...
            self.cache.pop(self.storage.remove_from_tail()[0]) # Removes the node from the hashtable(dict) as well as the DLL
            self.size -= 1 # Decrement size of DLL manually.
        self.storage.add_to_head((key, value)) # If key is not currently in cache, add to the head of the DLL
        self.cache[key] = self.storage.head # Assign the node at position 'head' to the hashtable 
        self.size += 1 # Increment the size of the DLL by 1
  
        




