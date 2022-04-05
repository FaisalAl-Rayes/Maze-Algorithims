'''Please read the docstring in the middle of this code starting with 
        "The algorithms below are intended..." to see how can you choose
            to see the final path or the full path of the algorithm.'''



from collections import deque
from Base import is_legal_pos, get_path, h_value
from Data_Structures import Stack, Queue, PriorityQueue
from Configuration import offsets


# # Depth First Search Algorithm
# def dfs(maze: list, start: tuple, goal: tuple):
#     stack = Stack()
#     stack.push(start)
#     predecessors = {start: None}

#     while not stack.is_empty():
#         current = stack.pop()
#         if current == goal:
#             return get_path(predecessors, start, goal)
#         for direction in ["up", "right", "down", "left"]:
#             row_offset, col_offset = offsets[direction]
#             neighbor = (current[0] + row_offset, current[1] + col_offset)
#             if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
#                 stack.push(neighbor)
#                 predecessors[neighbor] = current
#     return None


# # Breadth First Search Algorithm
# def bfs(maze: list, start: tuple, goal: tuple):
#     queue = deque()
#     queue.append(start)
#     predecessors = {start: None}

#     while queue:
#         current = queue.popleft()
#         if current == goal:
#             return get_path(predecessors, start, goal)
#         for direction in ["up", "right", "down", "left"]:
#             row_offset, col_offset = offsets[direction]
#             neighbor = (current[0] + row_offset, current[1] + col_offset)
#             if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
#                 queue.append(neighbor)
#                 predecessors[neighbor] = current
#     return None


# # A* Algorithm
# def a_star(maze, start, goal):
#     pq = PriorityQueue()
#     pq.put(start, 0)
#     predecessors = {start: None}
#     # The g_value is the distance between the current cell and the start cell
#     g_values = {start: 0}

#     while not pq.is_empty():
#         current = pq.get()
#         if current == goal:
#             return get_path(predecessors, start, goal)
#         for direction in ["up", "right", "down", "left"]:
#             row_offset, col_offset = offsets[direction]
#             neighbor = (current[0] + row_offset, current[1] + col_offset)
#             if is_legal_pos(maze, neighbor) and neighbor not in g_values:
#                 g_values[neighbor] = g_values[current] + 1
#                 f_value = g_values[neighbor] + h_value(neighbor, goal)
#                 pq.put(neighbor, f_value)
#                 predecessors[neighbor] = current
#     return None



'''The algorithms below are intended to help in the visualization of how the different algorithims
        behave. If you would like to only see the final path then comment out the code below this docstring.
            If you would like to see the the full path for better visualization of the behavior of the algorithims
                then comment out everything above(apart from the imports).'''



# Depth First Search Algorithm (full path)
def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    visited = set()
    full_path = []

    while stack:
        current = stack.pop()
        full_path.append(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in visited:
                stack.push(neighbour)
                visited.add(neighbour)


# breadth First Search Algorithm (full path)
def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    visited = set()
    full_path = []

    while queue:
        current = queue.dequeue()
        full_path.append(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in visited:
                queue.enqueue(neighbour)
                visited.add(neighbour)

# A* Algorithm (full path)
def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    g_values = {start: 0}
    full_path = []

    while not pq.is_empty():
        current = pq.get()
        full_path.append(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in g_values:
                g_values[neighbour] = g_values[current] + 1
                f_value = g_values[neighbour] + h_value(neighbour, goal)
                pq.put(neighbour, f_value)