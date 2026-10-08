from queue import PriorityQueue


def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def best_first_search(maze, start, goal):

    queue = PriorityQueue()
    queue.put((manhattan_distance(start, goal), start, [start]))

    visited = set()

    while not queue.empty():

        heuristic, current, path = queue.get()

        if current == goal:
            print("Goal Found!")
            return path

        if current in visited:
            continue

        visited.add(current)

        row, col = current

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            if (0 <= new_row < len(maze) and
                0 <= new_col < len(maze[0]) and
                maze[new_row][new_col] == 0):

                neighbor = (new_row, new_col)

                if neighbor not in visited:

                    h = manhattan_distance(neighbor, goal)

                   

                    queue.put(
                        (h, neighbor, path + [neighbor])
                    )

    return None


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = best_first_search(maze, start, goal)

print("\nFinal Path:")
print(path)