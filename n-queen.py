import random


class Environment:

    def __init__(self, n):
        self.n = n

    def calculate_conflicts(self, state):

        conflicts = 0

        for i in range(self.n):

            for j in range(i + 1, self.n):

                if state[i] == state[j]:
                    conflicts += 1

                elif abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1

        return conflicts

    def get_neighbors(self, state):

        neighbors = []
        n = len(state)

        for row in range(n):

            for col in range(n):

                if col != state[row]:

                    new_state = state.copy()
                    new_state[row] = col

                    neighbors.append(new_state)

        return neighbors


class GoalBasedAgent:

    def __init__(self, environment):
        self.environment = environment

    def goal_test(self, state):

        conflicts = self.environment.calculate_conflicts(state)

        return conflicts == 0

    def simple_hill_climbing(self):

        n = self.environment.n

        current_state = [random.randint(0, n - 1) for _ in range(n)]

        current_conflicts = self.environment.calculate_conflicts(
            current_state
        )

        print("Initial State:", current_state)
        print("Initial Conflicts:", current_conflicts)
        print()

        while True:

            if self.goal_test(current_state):

                print("Goal Reached!")
                return current_state, current_conflicts

            neighbors = self.environment.get_neighbors(current_state)

            next_state = None
            next_conflicts = current_conflicts

            for neighbor in neighbors:

                neighbor_conflicts = self.environment.calculate_conflicts(
                    neighbor
                )

                if neighbor_conflicts < current_conflicts:

                    next_state = neighbor
                    next_conflicts = neighbor_conflicts

                    break

            if next_state is None:

                print("No better neighbor exists.")
                break

            current_state = next_state
            current_conflicts = next_conflicts

            print("Moved to:", current_state)
            print("Conflicts:", current_conflicts)
            print()

        return current_state, current_conflicts


n = 4

environment = Environment(n)

agent = GoalBasedAgent(environment)

solution, conflicts = agent.simple_hill_climbing()

print("--------------------------------")

if conflicts == 0:
    print("Solution found for N-Queens problem!")
else:
    print("Hill Climbing stopped with", conflicts, "conflicts.")

print("Final State:", solution)