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

    def dfs(self, start, goal):

        stack = [(start, [start])]
        visited = set()

        while stack:

            current, path = stack.pop()

            if current == goal:
                return path

            if current not in visited:
                visited.add(current)

                for neighbor in reversed(
                    self.environment.get_neighbors(current)
                ):
                    if neighbor not in visited:
                        stack.append(
                            (neighbor, path + [neighbor])
                        )

        return None


class UtilityBasedAgent:
    def choose_path(self, path):

        utility = 100 - (len(path) - 1) * 10

        return f"Path: {path}, Utility: {utility}"


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

path = goal_agent.dfs(start, goal)


simple_agent = SimpleReflexAgent()
model_agent = ModelBasedReflexAgent()
utility_agent = UtilityBasedAgent()
learning_agent = LearningAgent()


print("Simple Reflex Agent:")
print(simple_agent.act(path))

print("\nModel-Based Reflex Agent:")
print(model_agent.act(path))

print("\nGoal-Based Agent:")
print(f"Path: {path}")

print("\nUtility-Based Agent:")
print(utility_agent.choose_path(path))

print("\nLearning Agent:")
print(learning_agent.learn(path))