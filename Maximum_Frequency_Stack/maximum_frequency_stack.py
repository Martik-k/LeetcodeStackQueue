"""
Maximum Frequency Stack.
"""

from collections import deque

class FreqStack:
    """
    A Frequency Stack is a data structure that mimics a stack but returns the most 
    frequent element when popping. If multiple elements have the same frequency, 
    the most recently pushed one among them is returned.
    """
    def __init__(self):
        """
        Initializes the FreqStack with two deques:
        - self.stack to track insertion order.
        - self.frequency to group elements by frequency.
        """
        self.stack = deque()
        self.frequency = deque()

    def push(self, val: int) -> None:
        """
        Pushes a value onto the stack.
        """
        frequency = 0
        for el in self.stack:
            if el == val:
                frequency += 1

        self.stack.appendleft(val)

        while len(self.frequency) <= frequency:
            self.frequency.append(deque())

        self.frequency[frequency].append(val)


    def pop(self) -> int:
        """
        Removes and returns the most frequent element.
        If multiple elements have the same frequency,
        the most recently added one is returned.
        """
        if not self.stack:
            raise ValueError('Stack is empty')

        if not self.frequency[-1]:
            self.frequency.pop()

        most_freq = self.frequency[-1].pop()
        self.stack.remove(most_freq)
        return most_freq
