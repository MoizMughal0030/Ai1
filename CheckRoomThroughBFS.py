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


class GoalBasedAgent:

    def __init__(self, environment):
        self.environment = environment

    def bfs(self, start):

        queue = deque()
        queue.append(start)

        visited = set()
        visited.add(start)

        while queue:

            current = queue.popleft()

            percept = self.environment.get_percept(current)

            print("Agent entered:", current)
            print("Status:", percept["status"])

            for neighbor in percept["adjacent"]:

                if neighbor not in visited:

                    neighbor_status = self.environment.get_percept(neighbor)["status"]

                    if neighbor_status != "critical":

                        visited.add(neighbor)
                        queue.append(neighbor)

                    else:
                        print("Ignoring:", neighbor, "(Critical)")

        print("\nSafe/Empty rooms visited:", visited)


environment = Environment()

agent = GoalBasedAgent(environment)

agent.bfs("Room A")