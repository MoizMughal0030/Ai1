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

    def get_percept(self, room):
        return self.rooms[room]


class UCSAgent:

    def __init__(self, environment):
        self.environment = environment

    def ucs(self, start):

        queue = PriorityQueue()

        queue.put((0, start, [start]))

        visited = set()

        while not queue.empty():

            cost, current, path = queue.get()

            if current in visited:
                continue

            visited.add(current)

            percept = self.environment.get_percept(current)

            if percept["status"] == "critical":
                print("Ignore:", current)
                continue

            print("Enter:", current)
            print("Status:", percept["status"])
            print("Cost:", cost)

            for neighbor, edge_cost in percept["adjacent"].items():

                if neighbor not in visited:

                    neighbor_status = self.environment.get_percept(neighbor)["status"]

                    if neighbor_status == "critical":

                        print("Ignore:", neighbor)

                    else:

                        new_cost = cost + edge_cost

                        new_path = path + [neighbor]

                        queue.put(
                            (new_cost, neighbor, new_path)
                        )

        print("\nVisited Rooms:", visited)


environment = Environment()

agent = UCSAgent(environment)

agent.ucs("Room A")

