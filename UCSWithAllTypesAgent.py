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

    def get_neighbors(self, node):
        return self.graph[node]


class SimpleReflexAgent:
    def act(self, path):
        return f"Path: {path}"


class ModelBasedReflexAgent:
    def __init__(self):
        self.model = []

    def act(self, path):
        self.model = path
        return f"Path: {self.model}"


class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment

    def ucs(self, start, goal):

        queue = PriorityQueue()
        queue.put((0, start, [start]))

        visited = set()

        while not queue.empty():

            cost, current, path = queue.get()

            if current == goal:
                return path, cost

            if current in visited:
                continue

            visited.add(current)

            for neighbor, edge_cost in self.environment.get_neighbors(current):

                if neighbor not in visited:
                    new_cost = cost + edge_cost

                    queue.put(
                        (new_cost, neighbor, path + [neighbor])
                    )

        return None, 0


class UtilityBasedAgent:
    def choose_path(self, path, cost):
        utility = 100 - cost

        return f"Path: {path}, Cost: {cost}, Utility: {utility}"


class LearningAgent:
    def __init__(self):
        self.experience = []

    def learn(self, path):
        self.experience.append(path)

        return f"Path: {path}"


environment = Environment()

start = "A"
goal = "G"

goal_agent = GoalBasedAgent(environment)

path, cost = goal_agent.ucs(start, goal)

simple_agent = SimpleReflexAgent()
model_agent = ModelBasedReflexAgent()
utility_agent = UtilityBasedAgent()
learning_agent = LearningAgent()


print("Simple Reflex Agent:")
print(simple_agent.act(path))


print("\nModel-Based Reflex Agent:")
print(model_agent.act(path))


print("\nGoal-Based Agent using UCS:")
print(f"Path: {path}")
print(f"Cost: {cost}")


print("\nUtility-Based Agent:")
print(utility_agent.choose_path(path, cost))


print("\nLearning Agent:")
print(learning_agent.learn(path))