# search.py
# ---------------
# Created by Yaya Wihardi (yayawihardi@upi.edu) on 15/03/2020

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col)
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]
#                          -> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function

import queue


def search(maze):
    cutoff = False
    result = []
    fringe = queue.LifoQueue()      # fringe in stack
    fringe.put(maze.getStart())
    current = fringe.get()          # current node
    level = 0                       # current depth
    limit = 3                       # depth limit
    parent = {}                     # parent node
    visited = []                    # visited node

    while current != maze.getObjectives()[0]:
        level = 0
        while level <= limit:
            if current == maze.getObjectives()[0]:
                break
            for x in maze.getNeighbors(current[0], current[1]):
                if (x not in visited) and (x not in fringe.queue):
                    fringe.put(x)
                    parent[x] = current
            visited.append(current)

            if not fringe.empty():
                current = fringe.get()
            level = level + 1
    node = current
    while node != maze.getStart():
        result.append(node)
        node = parent[node]
    result.append(node)
    result.reverse()

    return result
