from collections import deque


class Environment:

    def __init__(self):

        self.rooms = {
            "Room A": {
                "status": "safe",
                "adjacent": ["Room B", "Room C"]
            },

            "Room B": {
                "status": "empty",
                "adjacent": ["Room A", "Room D"]
            },

            "Room C": {
                "status": "critical",
                "adjacent": ["Room A", "Room D"]
            },

            "Room D": {
                "status": "safe",
                "adjacent": ["Room B", "Room C"]
            }
        }

    def get_percept(self, room):
        return self.rooms[room]


class SimpleReflexAgent:

    def __init__(self, environment):
        self.environment = environment

    def act(self, current_room):

        percept = self.environment.get_percept(current_room)

        print("\nSimple Reflex Agent")
        print("Current Room:", current_room)
        print("Status:", percept["status"])

        if percept["status"] == "critical":
            print("Action: Handle critical room")

        elif percept["status"] == "safe":
            print("Action: Move to next room")

        else:
            print("Action: Continue searching")


class ModelBasedAgent:

    def __init__(self, environment):
        self.environment = environment
        self.visited = set()

    def act(self, current_room):

        self.visited.add(current_room)

        percept = self.environment.get_percept(current_room)

        print("\nModel-Based Agent")
        print("Current Room:", current_room)
        print("Status:", percept["status"])
        print("Visited:", self.visited)

        if percept["status"] == "critical":
            print("Action: Handle critical room")

        else:
            for room in percept["adjacent"]:
                if room not in self.visited:
                    print("Action: Move to", room)
                    return room


class GoalBasedAgent:

    def __init__(self, environment):
        self.environment = environment

    def bfs(self, start, goal):

        queue = deque()
        queue.append(start)

        visited = set()
        visited.add(start)

        while queue:

            current_room = queue.popleft()

            percept = self.environment.get_percept(current_room)

            print("\nGoal-Based Agent")
            print("Current Room:", current_room)
            print("Status:", percept["status"])

            if percept["status"] == goal:
                print("Goal Found:", current_room)
                return current_room

            for neighbor in percept["adjacent"]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


class UtilityBasedAgent:

    def __init__(self, environment):
        self.environment = environment

    def bfs(self, start):

        queue = deque()
        queue.append(start)

        visited = set()
        visited.add(start)

        utility = {
            "critical": 100,
            "safe": 50,
            "empty": 10
        }

        while queue:

            current_room = queue.popleft()

            percept = self.environment.get_percept(current_room)

            status = percept["status"]

            print("\nUtility-Based Agent")
            print("Current Room:", current_room)
            print("Status:", status)
            print("Utility:", utility[status])

            if status == "critical":
                print("Highest Utility Found!")
                print("Action: Handle critical room")
                return current_room

            for neighbor in percept["adjacent"]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


environment = Environment()


simple_agent = SimpleReflexAgent(environment)
simple_agent.act("Room A")


model_agent = ModelBasedAgent(environment)
model_agent.act("Room A")


goal_agent = GoalBasedAgent(environment)
goal_agent.bfs("Room A", "critical")


utility_agent = UtilityBasedAgent(environment)
utility_agent.bfs("Room A")