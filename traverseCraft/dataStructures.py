class TreeNode:
    def __init__(self, val: int, children: list, isGoalState:bool=False, edges: list=[]):
        self.val = val
        self.children = children
        if((len(children) > 0) and (edges == [] or edges is None)):
            edges = [1] * len(children)
        self.edges = edges
        self.isGoalState = isGoalState
        self._heatMapValue = 0.0
