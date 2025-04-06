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


class Stack:
    """
    A Stack class implemented using a linked list.
    """
    def __init__(self):
        """
        Initializes an empty Stack.
        """
        self.head = None

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
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.head.item

    def pop_from_top(self):
        """
        Removes and returns the top item from the Stack.
        """
        if self.is_empty():
            raise ValueError('Stack is empty')
        result = self.head.item
        self.head = self.head.next
        return result

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
    """
    Implementation of a Queue using two Stacks.
    """
    def __init__(self):
        """
        Initializes a MyQueue object with two stacks: the main queue and a supporting stack.
        """
        self.queue = Stack()
        self.supporting = Stack()

    def push(self, x: int) -> None:
        """
        Adds element 'x' to the end of the queue.
        """
        while not self.queue.is_empty():
            node = self.queue.pop_from_top()
            self.supporting.push_to_top(node)
        self.queue.push_to_top(x)
        while not self.supporting.is_empty():
            node = self.supporting.pop_from_top()
            self.queue.push_to_top(node)

    def pop(self) -> int:
        """
        Removes and returns the first element from the queue.
        """
        return self.queue.pop_from_top()

    def peek(self) -> int:
        """
        Returns the first element of the queue without removing it.
        """
        return self.queue.peek()

    def empty(self) -> bool:
        """
        Checks if the queue is empty.
        """
        return self.queue.is_empty()
