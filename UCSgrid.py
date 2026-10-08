from collections import deque


class Environment:

    def __init__(self):

        self.grid = [
            ["A", "0", "0", "#", "#"],
            ["#", "F", "0", "#", "P"],
            ["0", "0", "0", "F", "0"],
            ["0", "#", "F", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

    def get_neighbors(self, current):

        row, col = current

        neighbors = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        valid_neighbors = []

        for dr, dc in neighbors:
            nr=row+dr
            nc=col+dc

            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):

                if self.grid[nr][nc] != "#" and self.grid[nr][nc] != "F":
                    valid_neighbors.append((nr, nc))

        return valid_neighbors


class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def dfs(self, environment, start):

        stack = [(start, [start])]

        visited = set()

        while stack:

            current, path = stack.pop()

            if current in visited:
                continue

            visited.add(current)

            if current == self.goal:
                return path

            for neighbor in reversed(environment.get_neighbors(current)):

                if neighbor not in visited:
                    stack.append(
                        (neighbor, path + [neighbor])
                    )

        return None


def run_agent():

    environment = Environment()

    agent = GoalBasedAgent((1, 4))

    path = agent.dfs(environment, (0, 0))

    if path:
        print("DFS Path:")
        print(path)
    else:
        print("No path found")


run_agent()