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

    def dls(self, current, goal, limit, path, depth):

        print(
            f"Visiting: {current} | "
            f"Current Depth: {depth} | "
            f"Depth Limit: {limit}"
        )

        if current == goal:
            return path

        if depth == limit:
            return None

        for neighbor in self.environment.get_neighbors(current):

            if neighbor not in path:

                result = self.dls(
                    neighbor,
                    goal,
                    limit,
                    path + [neighbor],
                    depth + 1
                )

                if result is not None:
                    return result

        return None

    def search(self, start, goal, limit):

        print(f"Starting DLS with Depth Limit = {limit}\n")

        return self.dls(
            start,
            goal,
            limit,
            [start],
            0
        )


class UtilityBasedAgent:
    def choose_path(self, path):

        if path is None:
            return "No path found"

        utility = 100 - (len(path) - 1) * 10

        return f"Path: {path}, Utility: {utility}"


class LearningAgent:
    def __init__(self):
        self.experience = []

    def learn(self, path):

        if path is not None:
            self.experience.append(path)
            return f"Path: {path}"

        return "Nothing learned"


environment = Environment()

start = "A"
goal = "G"
depth_limit = 3

simple_agent = SimpleReflexAgent()
model_agent = ModelBasedReflexAgent()
goal_agent = GoalBasedAgent(environment)
utility_agent = UtilityBasedAgent()
learning_agent = LearningAgent()


path = goal_agent.search(
    start,
    goal,
    depth_limit
)


print("\nSimple Reflex Agent:")
print(simple_agent.act(path))


print("\nModel-Based Reflex Agent:")
print(model_agent.act(path))


print("\nGoal-Based Agent using DLS:")
print("Final Path:", path)
print("Depth Limit:", depth_limit)


print("\nUtility-Based Agent:")
print(utility_agent.choose_path(path))


print("\nLearning Agent:")
print(learning_agent.learn(path))

print("Experience:", learning_agent.experience)