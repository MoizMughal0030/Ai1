from queue import PriorityQueue


class Environment:
    def __init__(self):
        self.graph = {
            "A": [("B", 2), ("C", 5)],
            "B": [("A", 2), ("D", 4), ("E", 1)],
            "C": [("A", 5), ("F", 2)],
            "D": [("B", 4), ("G", 3)],
            "E": [("B", 1), ("G", 6)],
            "F": [("C", 2), ("G", 1)],
            "G": [("D", 3), ("E", 6), ("F", 1)]
        }

        self.heuristic = {
            "A": 6,
            "B": 4,
            "C": 3,
            "D": 2,
            "E": 1,
            "F": 2,
            "G": 0
        }

    def get_neighbors(self, node):
        return self.graph[node]

    def get_heuristic(self, node):
        return self.heuristic[node]


class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment

    def act(self, path):
        return f"Path: {path}"

    def a_star_search(self, start, goal):

        queue = PriorityQueue()
        queue.put((self.environment.get_heuristic(start), 0, start, [start]))

        visited = set()

        while not queue.empty():

            f, cost, current, path = queue.get()

            print("Selected:", current, "g =", cost,
                  "h =", self.environment.get_heuristic(current),
                  "f =", f)

            if current == goal:
                print("Goal Found!")
                return path, cost

            if current in visited:
                continue

            visited.add(current)

            for neighbor, edge_cost in self.environment.get_neighbors(current):

                if neighbor not in visited:

                    new_cost = cost + edge_cost
                    h = self.environment.get_heuristic(neighbor)
                    new_f = new_cost + h

                    print("Adding:", neighbor,
                          "g =", new_cost,
                          "h =", h,
                          "f =", new_f)

                    queue.put(
                        (new_f, new_cost, neighbor, path + [neighbor])
                    )

        return None, 0


class ModelBasedReflexAgent:
    def __init__(self):
        self.model = []

    def act(self, path):
        self.model = path
        return f"Path: {self.model}"


class GoalBasedAgent:
    def act(self, path):
        return f"Path: {path}"


class UtilityBasedAgent:
    def choose_path(self, path, cost):

        if path is None:
            return "No path found"

        utility = 100 - cost * 5

        return f"Path: {path}, Cost: {cost}, Utility: {utility}"


class LearningAgent:
    def __init__(self):
        self.experience = []

    def learn(self, path):

        if path is not None:
            self.experience.append(path)

        return f"Path: {path}"


environment = Environment()

start = "A"
goal = "G"

simple_agent = SimpleReflexAgent(environment)
model_agent = ModelBasedReflexAgent()
goal_agent = GoalBasedAgent()
utility_agent = UtilityBasedAgent()
learning_agent = LearningAgent()

path, cost = simple_agent.a_star_search(start, goal)

print("\nSimple Reflex Agent:")
print(simple_agent.act(path))

print("\nModel-Based Reflex Agent:")
print(model_agent.act(path))

print("\nGoal-Based Agent:")
print(goal_agent.act(path))

print("\nUtility-Based Agent:")
print(utility_agent.choose_path(path, cost))

print("\nLearning Agent:")
print(learning_agent.learn(path))

print("\nFinal Path:", " -> ".join(path))
print("Total Cost:", cost)