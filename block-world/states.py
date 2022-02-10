class State:
    def __init__(self, arrangement) -> None:
        self.blocks = [block for stack in arrangement for block in stack]



class Goal:
    def __init__(self, goal_arrangement) -> None:
        self.goal = goal_arrangement
        

    def is_goal(self, state) -> bool:
        '''Check if state is in goal condition
        '''
        return state == self.goal

    
    def get_move_cost():
        pass