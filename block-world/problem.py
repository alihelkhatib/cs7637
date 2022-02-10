from states import Goal

class Problem:
    def __init__(self, initial_arrangement, goal_arrangement) -> None:
        self.initial = initial_arrangement
        self.goal = Goal(goal_arrangement)
        

    def move(self, block, location) -> list:
        pass

    def get_block_states(self, arrangement):
        for stack in arrangement:
