from queue import PriorityQueue


class Environment:

    def __init__(self):

        self.rooms = {
            "Room A": {
                "status": "safe",
                "adjacent": {
                    "Room B": 2,
                    "Room C": 1
                }
            },

            "Room B": {
                "status": "empty",
                "adjacent": {
                    "Room A": 2,
                    "Room D": 3
                }
            },

            "Room C": {
                "status": "critical",
                "adjacent": {
                    "Room A": 1,
                    "Room D": 1
                }
            },

            "Room D": {
                "status": "safe",
                "adjacent": {
                    "Room B": 3,
                    "Room C": 1
                }
            }
        }

        self.heuristic = {
            "Room A": 5,
            "Room B": 3,
            "Room C": 1,
            "Room D": 0
        }

    def get_percept(self, room):
        return self.rooms[room]

    def get_heuristic(self, room):
        return self.heuristic[room]


class AStarAgent:

    def __init__(self, environment):
        self.environment = environment

    def search(self, start, goal):

        queue = PriorityQueue()

        queue.put((0, 0, start, [start]))

        visited = set()

        while not queue.empty():

            f, g, current, path = queue.get()

            if current in visited:
                continue

            visited.add(current)

            percept = self.environment.get_percept(current)

            if percept["status"] == "critical":

                print("Ignore:", current)
                continue

            print("Enter:", current)
            print("Status:", percept["status"])
            print("g =", g)
            print("h =", self.environment.get_heuristic(current))
            print("f =", f)

            if current == goal:

                print("\nGoal reached!")
                print("Path:", path)
                print("Total Cost:", g)

                return path

            for neighbor, edge_cost in percept["adjacent"].items():

                if neighbor not in visited:

                    neighbor_status = self.environment.get_percept(neighbor)["status"]

                    if neighbor_status == "critical":

                        print("Ignore:", neighbor)

                    else:

                        new_g = g + edge_cost

                        h = self.environment.get_heuristic(neighbor)

                        new_f = new_g + h

                        new_path = path + [neighbor]

                        queue.put(
                            (new_f, new_g, neighbor, new_path)
                        )


environment = Environment()

agent = AStarAgent(environment)

agent.search("Room A", "Room D")