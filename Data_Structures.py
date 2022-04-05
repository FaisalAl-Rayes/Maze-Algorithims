'''This module carries the data structures needed for the 
        search algorithms (Depth First Search, Breradth First Search, and A*).'''


from collections import deque
from heapq import heappush, heappop


class Stack:
    '''This is the data structure used
            for the Depth First Search algorithm.'''

    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    
class Queue:
    '''This is the data structure used
            for the Breadth First Search algorithm.'''

    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)

    
class PriorityQueue:
    '''This is the data structure used
            for the A* algorithm.'''

    def __init__(self) -> None:
        self.elements = []
    
    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heappush(self.elements,(priority, item))
    
    def get(self):
        return heappop(self.elements)[1]
    
    def size(self):
        return len(self.elements)

    def __str__(self) -> str:
        return str(self.elements)


