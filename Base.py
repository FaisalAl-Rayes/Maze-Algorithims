'''This module holds the base functions.'''
import Configuration

def read_maze(filepath) -> list:
    '''Reads a file to extract the maze layout.'''
    try:
        with open(filepath, 'r') as f:
            maze = [[char for char in line.strip("\r\n")] for line in f]
            col_num = len(maze[0])
            row_num = len(maze)
            for row in maze:
                if len(row) != col_num:
                    print("The maze is not rectangular!")
                    raise SystemExit
            maze_obstacles = []
            for i in range(row_num):
                for j in range(col_num):
                    if maze[i][j] == Configuration.OBSTACLE:
                        maze_obstacles.append((i, j))
                    elif maze[i][j] == Configuration.OPPONENT:
                        opponent_start_pos = (i, j)
            return maze, (row_num, col_num), maze_obstacles, opponent_start_pos
    except UnboundLocalError:
        print("The maze needs a player and an opponent.")
        raise SystemExit
    except OSError:
        print("There is a problem with the file!")
        raise SystemExit


def is_legal_pos(maze: list, pos: tuple) -> bool:
    '''To check if it is a position that 
            we can consider as we navigate the maze.'''

    i, j = pos
    max_rows = len(maze)
    max_cols = len(maze[0])
    return 0 <= i <= max_rows and 0 <= j <= max_cols and maze[i][j] != "*"


def get_path(predecessors: dict, start: tuple, goal: tuple) -> list:
    '''Only used when we reach the goal to get the path from
            the start to the goal.'''

    current = goal
    path = []
    while current is not start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


def h_value(point1: tuple, point2: tuple) -> int:
    '''the heuristic value also known as the Manhattan distance
            in the conext of the maze it will represent that distance
                between the current cell and the goal.'''

    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)


def grid_to_screen_coords(pos, grid_dimensions):
    """Converts grid coordinates to screen coordinates."""

    i, j = pos
    # 20 here is a turtle size of 18 plus 1 px border each side, so the size of one "cell".
    screen_x = - ((grid_dimensions[1] - 1) / 2 * 20) + (j * 20)
    screen_y = ((grid_dimensions[0] - 1) / 2 * 20) - (i * 20)
    return (screen_x, screen_y)


def screen_to_grid_coords(pos, dimensions):
    """Converts screen coordinates to grid coordinates."""

    x, y = pos
    m, n = dimensions
    j = int((20 * (n / 2) + x) / 20)
    i = int((20 * (m / 2) - y) / 20)
    return (i, j)