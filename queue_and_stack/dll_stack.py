import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):  # Adding an item onto the stack, goes in front...will be the first thing to come off the stack.
        self.storage.add_to_tail(value)

    def pop(self):    # Removing an item off of the stack.
        if self.storage.__len__() is 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail() 
    def len(self):   # Getting length of items on the stack.
        return self.storage.__len__()
