from collections import deque


class Environment:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B", "G"],
            "E": ["B", "G"],
            "F": ["C", "G"],
            "G": ["D", "E", "F"]
        }

    def get_percept(self, node):
        if node == "G":
            return "GOAL"
        return "NORMAL"

    def get_neighbors(self, node):
        return self.graph[node]


class SimpleReflexAgent:
    def act(self, percept):
        if percept == "GOAL":
            return "STOP"
        return "MOVE"


class ModelBasedReflexAgent:
    def __init__(self):
        self.model = {}

    def act(self, node, percept):
        self.model[node] = percept

        if percept == "GOAL":
            return "STOP"

        return "MOVE"


class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment

    def bfs(self, start, goal):

        queue = deque()
        queue.append((start, [start]))

        visited = set()
        visited.add(start)

        while queue:

            current, path = queue.popleft()

            if current == goal:
                return path

            for neighbor in self.environment.get_neighbors(current):

                if neighbor not in visited:
                    visited.add(neighbor)

                    new_path = path + [neighbor]

                    queue.append((neighbor, new_path))

        return None


class UtilityBasedAgent:
    def choose_path(self, path):

        if path is None:
            return "No path"

        utility = 100 - (len(path) - 1) * 10

        return f"Path = {path}, Utility = {utility}"


class LearningAgent:
    def __init__(self):
        self.experience = []

    def learn(self, path):

        if path:
            self.experience.append(path)
            return "Agent learned the path"

        return "Nothing learned"


environment = Environment()

start = "A"
goal = "G"


simple_agent = SimpleReflexAgent()

model_agent = ModelBasedReflexAgent()

goal_agent = GoalBasedAgent(environment)

utility_agent = UtilityBasedAgent()

learning_agent = LearningAgent()


print("Simple Reflex Agent:")
print(simple_agent.act(environment.get_percept(start)))


print("\nModel Based Reflex Agent:")
print(model_agent.act(start, environment.get_percept(start)))
print("Model:", model_agent.model)


print("\nGoal Based Agent using BFS:")

path = goal_agent.bfs(start, goal)

print("BFS Path:", path)


print("\nUtility Based Agent:")
print(utility_agent.choose_path(path))


print("\nLearning Agent:")
print(learning_agent.learn(path))

print("Experience:", learning_agent.experience)