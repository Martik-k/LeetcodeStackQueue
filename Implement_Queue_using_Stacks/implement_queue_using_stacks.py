"""
Implement Queue using Stacks.
"""

class Node:
    """
    A Node class representing a single element in a linked list, used internally by the Stack.
    """
    def __init__(self, item, next_node=None):
        """
        Initializes a Node with a given item and an optional next Node.
        """
        self.item = item
        self.next = next_node

    def __repr__(self):
        """
        Returns a string representation of the Node's item.
        """
        return str(self.item)


class Stack:
    """
    A Stack class implemented using a linked list.
    """
    def __init__(self):
        """
        Initializes an empty Stack.
        """
        self.head = None

    def __repr__(self):
        """
        Returns a string representation of the Stack.
        """
        if self.is_empty():
            return 'None'
        result = f'{self.head}'
        cur = self.head.next
        while cur:
            result += f' - {cur}'
            cur = cur.next
        return result

    def is_empty(self):
        """
        Checks if the Stack is empty.
        """
        return self.head is None

    def push_to_top(self, item):
        """
        Pushes an item onto the top of the Stack.
        """
        self.head = Node(item, self.head)

    def peek(self):
        """
        Returns the top item of the Stack without removing it.
        """
        return self.head

    def pop_from_top(self):
        """
        Removes and returns the top item from the Stack.
        """
        if self.is_empty():
            raise ValueError('Stack is empty')
        head = self.head
        self.head = self.head.next
        return head

    def size(self):
        """
        Returns the number of items in the Stack.
        """
        i = 0
        cur = self.head
        while cur:
            i += 1
            cur = cur.next
        return i


class MyQueue:

    def __init__(self):
        pass
        

    def push(self, x: int) -> None:
        pass
        

    def pop(self) -> int:
        pass
        

    def peek(self) -> int:
        pass
        

    def empty(self) -> bool:
        pass
        
