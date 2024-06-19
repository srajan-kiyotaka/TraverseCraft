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
        self._heatMapValue = 0
    
    def __str__(self) -> str:
        children = [child.id for child in self.children]
        return f"Tree Node Id: {self.id} \nChildren: {children} \nValue: {self.val} \nGoal State: {self.isGoalState} \nEdges: {self.edges} \nHeat Map Value: {self._heatMapValue}"

class GraphNode:
    def __init__(self, label, neighbors: list, val = None, isGoalState:bool=False, edges: list=[]):
        self.id = label
        self.val = val
        if val is None:
            self.val = label
        self.neighbors = neighbors
        if((len(neighbors) > 0) and (edges == [] or edges is None)):
            edges = [1] * len(neighbors)
        self.edges = edges
        self.isGoalState = isGoalState
        self._heatMapValue = 0

    def __str__(self) -> str:
        return f"Graph Node Id: {self.id} \nNeighbors: {self.neighbors} \nValue: {self.val} \nGoal State: {self.isGoalState} \nEdges: {self.edges} \nHeat Map Value: {self._heatMapValue}"