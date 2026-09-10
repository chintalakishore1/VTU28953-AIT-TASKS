class MonkeyBananaPlanner:

    def __init__(self):

        # Initial State
        self.state = {
            "on_floor(Monkey)",
            "at(Monkey, Center)",
            "at(Box, Window)"
        }

        # Goal State
        self.goal = "has(Monkey, Banana)"

        # Operators
        self.operators = {
            "Walk(Center, Window)": {
                "preconds": {
                    "on_floor(Monkey)",
                    "at(Monkey, Center)"
                },
                "add": {
                    "at(Monkey, Window)"
                },
                "del": {
                    "at(Monkey, Center)"
                }
            },

            "Push(Box, Window, Center)": {
                "preconds": {
                    "on_floor(Monkey)",
                    "at(Monkey, Window)",
                    "at(Box, Window)"
                },
                "add": {
                    "at(Monkey, Center)",
                    "at(Box, Center)"
                },
                "del": {
                    "at(Monkey, Window)",
                    "at(Box, Window)"
                }
            },

            "Climb(Box)": {
                "preconds": {
                    "on_floor(Monkey)",
                    "at(Monkey, Center)",
                    "at(Box, Center)"
                },
                "add": {
                    "on_box(Monkey)"
                },
                "del": {
                    "on_floor(Monkey)"
                }
            },

            "Grasp(Banana)": {
                "preconds": {
                    "on_box(Monkey)",
                    "at(Monkey, Center)",
                    "at(Box, Center)"
                },
                "add": {
                    "has(Monkey, Banana)"
                },
                "del": set()
            }
        }

        self.plan = []

    # Check whether preconditions are satisfied
    def can_execute(self, action):
        preconditions = self.operators[action]["preconds"]
        return preconditions.issubset(self.state)

    # Execute an action
    def execute(self, action):

        operator = self.operators[action]

        # Remove deleted conditions
        self.state -= operator["del"]

        # Add new conditions
        self.state |= operator["add"]

        # Store action in plan
        self.plan.append(action)

        print("\nExecuting:", action)
        print("Current State:", self.state)

    # Goal Stack Planning
    def solve(self):

        print("========== MONKEY BANANA PROBLEM ==========")

        print("\nInitial State:")
        for item in sorted(self.state):
            print("-", item)

        print("\nGoal:")
        print("-", self.goal)

        # Goal stack
        goal_stack = [
            "Walk(Center, Window)",
            "Push(Box, Window, Center)",
            "Climb(Box)",
            "Grasp(Banana)"
        ]

        print("\n========== PLANNING STARTED ==========")

        for action in goal_stack:

            if self.can_execute(action):
                self.execute(action)

            else:
                print("\nCannot execute:", action)
                print("Preconditions not satisfied!")
                return

        # Final Result
        print("\n========== GOAL ACHIEVED ==========")

        print("\nFinal Plan:")

        for i, action in enumerate(self.plan, start=1):
            print(f"{i}. {action}")

        print("\nFinal State:")

        for item in sorted(self.state):
            print("-", item)


# Main Program
planner = MonkeyBananaPlanner()
planner.solve()


output:
========== MONKEY BANANA PROBLEM ==========

Initial State:
- at(Box, Window)
- at(Monkey, Center)
- on_floor(Monkey)

Goal:
- has(Monkey, Banana)

========== PLANNING STARTED ==========

Executing: Walk(Center, Window)
Current State: {'on_floor(Monkey)', 'at(Monkey, Window)', 'at(Box, Window)'}

Executing: Push(Box, Window, Center)
Current State: {'at(Box, Center)', 'at(Monkey, Center)', 'on_floor(Monkey)'}

Executing: Climb(Box)
Current State: {'at(Box, Center)', 'at(Monkey, Center)', 'on_box(Monkey)'}

Executing: Grasp(Banana)
Current State: {'at(Box, Center)', 'at(Monkey, Center)', 'has(Monkey, Banana)', 'on_box(Monkey)'}

========== GOAL ACHIEVED ==========

Final Plan:
1. Walk(Center, Window)
2. Push(Box, Window, Center)
3. Climb(Box)
4. Grasp(Banana)

Final State:
- at(Box, Center)
- at(Monkey, Center)
- has(Monkey, Banana)
- on_box(Monkey)
