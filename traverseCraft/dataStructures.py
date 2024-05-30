class TreeNode:
    def __init__(self, val: int, isGoalState:bool=False):
        self.val = val
        self.left = None
        self.right = None
        self.isGoalState = isGoalState
        self._heatMapValue = 0.0
