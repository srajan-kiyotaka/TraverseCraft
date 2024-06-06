class TreeNode:
    def __init__(self, label, children: list, val = None, isGoalState:bool=False, edges: list=[]):
        self.id = label
        self.val = val
        if val is None:
            self.val = label
        self.children = children
        if((len(children) > 0) and (edges == [] or edges is None)):
            edges = [1] * len(children)
        self.edges = edges
        self.isGoalState = isGoalState
        self._heatMapValue = 0.0
