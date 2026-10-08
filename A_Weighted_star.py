from queue import PriorityQueue


class Environment:

    def __init__(self):

        self.grid = [
            [0, 1, 2, "#", 3],
            [1, "#", 2, "#", "#"],
            [1, 2, 1, 2, "#"],
            ["#", "#", 1, "#", "#"],
            [1, 1, 1, 2, 0]
        ]

    def get_neighbors(self, current):

        row, col = current

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        neighbors = []

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):

                if self.grid[nr][nc] != "#":
                    neighbors.append((nr, nc))

        return neighbors


class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def heuristic(self, current):

        return abs(current[0] - self.goal[0]) + abs(current[1] - self.goal[1])

    def a_star(self, environment, start):

        queue = PriorityQueue()

        queue.put((0, 0, start, [start]))

        visited = set()

        while not queue.empty():

            f, cost, current, path = queue.get()

            if current == self.goal:
                return path, cost

            if current in visited:
                continue

            visited.add(current)

            for neighbor in environment.get_neighbors(current):

                if neighbor in visited:
                    continue

                row, col = neighbor

                new_cost = cost + environment.grid[row][col]

                h = self.heuristic(neighbor)

                f = new_cost + h

                queue.put(
                    (f, new_cost, neighbor, path + [neighbor])
                )

        return None, None


def run_agent():

    environment = Environment()

    agent = GoalBasedAgent((4, 4))

    path, cost = agent.a_star(environment, (0, 0))

    print("Shortest Path:")
    print(path)

    print("Total Cost:")
    print(cost)


run_agent()