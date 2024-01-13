class TreeNode:
    def __init__(self, nodeName:str, x:int, y:int, parent=None, isGoalState:bool=False):
        self.nodeName = nodeName
        self.x = x
        self.y = y
        self.parent = parent
        self.children = []
        self.isGoalState = isGoalState
        self._heatMapValue = 0.0