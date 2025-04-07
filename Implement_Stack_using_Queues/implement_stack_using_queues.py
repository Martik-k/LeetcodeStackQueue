'''
Implement Stack using Queues.
'''
class Node:
    """
    A Node class representing a single element in a linked list.
    """
    def __init__(self, item, next_node=None):
        """
        Initializes a Node object.
        """
        self.item = item
        self.next = next_node


class Queue:
    """
    A Queue class implemented using a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty Queue.
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return self.head is None

    def size(self):
        """
        Returns the size of the queue.
        """
        if self.is_empty():
            return 0
        i = 0
        cur = self.head
        while cur:
            i += 1
            cur = cur.next
        return i

    def peek_from_front(self):
        """
        Returns the item at the front of the queue without removing it.
        """
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self.head.item

    def pop_from_front(self):
        """
        Removes and returns the item at the front of the queue.
        """
        if self.is_empty():
            raise ValueError('Queue is empty')
        result = self.head.item
        self.head = self.head.next
        return result

    def push_to_back(self, x):
        """
        Adds an item to the back of the queue.
        """
        if self.is_empty():
            self.head = Node(x)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(x)


class MyStack:
    """
    A Stack class implemented using two queues.
    """
    def __init__(self):
        """
        Initializes an empty Stack using two queues.
        """
        self.stack = Queue()
        self.supporting = Queue()

    def push(self, x: int) -> None:
        """
        Pushes an element onto the stack.
        """
        while not self.stack.is_empty():
            node = self.stack.pop_from_front()
            self.supporting.push_to_back(node)
        self.stack.push_to_back(x)
        while not self.supporting.is_empty():
            node = self.supporting.pop_from_front()
            self.stack.push_to_back(node)

    def pop(self) -> int:
        """
        Removes and returns the element at the top of the stack.
        """
        return self.stack.pop_from_front()

    def top(self) -> int:
        """
        Returns the element at the top of the stack without removing it.
        """
        return self.stack.peek_from_front()

    def empty(self) -> bool:
        """
        Checks if the stack is empty.
        """
        return self.stack.is_empty()
