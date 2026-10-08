from queue import PriorityQueue


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

        self.heuristic = {
            "A": 6,
            "B": 4,
            "C": 3,
            "D": 2,
            "E": 1,
            "F": 2,
            "G": 0
        }

    def get_percept(self, node):
        if node == "G":
            return "GOAL"
        return "NORMAL"

    def get_neighbors(self, node):
        return self.graph[node]

    def get_heuristic(self, node):
        return self.heuristic[node]


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

    def best_first_search(self, start, goal):

        queue = PriorityQueue()
        queue.put((self.environment.get_heuristic(start), start, [start]))

        visited = set()

        print("Best-First Search Started\n")

        while not queue.empty():

            heuristic, current, path = queue.get()

            print("Selected Node:", current)
            print("Heuristic:", heuristic)
            print("Current Path:", path)

            if current == goal:
                print("Goal Found!")
                return path

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.environment.get_neighbors(current):

                if neighbor not in visited:

                    h = self.environment.get_heuristic(neighbor)

                    print("Adding:", neighbor, "| Heuristic:", h)

                    queue.put(
                        (h, neighbor, path + [neighbor])
                    )

            print()

        return None


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

simple_agent = SimpleReflexAgent()
model_agent = ModelBasedReflexAgent()
goal_agent = GoalBasedAgent(environment)
utility_agent = UtilityBasedAgent()
learning_agent = LearningAgent()


path = goal_agent.best_first_search(start, goal)


print("\nSimple Reflex Agent:")
print(simple_agent.act(path))

print("\nModel-Based Reflex Agent:")
print(model_agent.act(path))

print("\nGoal-Based Agent using Best-First Search:")
print("Final Path:", path)

print("\nUtility-Based Agent:")
print(utility_agent.choose_path(path))

print("\nLearning Agent:")
print(learning_agent.learn(path))

print("Experience:", learning_agent.experience)