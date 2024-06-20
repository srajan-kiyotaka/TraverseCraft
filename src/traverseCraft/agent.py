from .world import CreateGridWorld, CreateTreeWorld, CreateGraphWorld
from tkinter import Frame, Tk
import time
from time import gmtime, strftime
import math
import colorsys
from prettytable import PrettyTable

# ~~~~~~~~~~~~~~~~ Grid Agent ~~~~~~~~~~~~~~~~ #

class GridAgent():
    """
    The Grid Agent class.

    Parameters:
        - world (CreateGridWorld): The grid world object in which the agent operates.
        - agentName (str): The name of the agent.
        - agentColor (str, optional): The color of the agent. Defaults to "blue".
        - heatMapView (bool, optional): Whether to enable the heat map view. Defaults to True.
        - heatMapColor (str, optional): The color of the heat map. Defaults to "#FFA732".
        - agentPos (tuple, optional): The initial position of the agent. Defaults to (0, 0).
        - heatGradient (float, optional): The gradient value for the heat map. Defaults to 0.05.

    Attributes:
        _worldObj (CreateGridWorld): The grid world object.
        _worldID (str): The ID of the world.
        _root (Tk): The root Tkinter object from the grid world.
        _agentName (str): The name of the agent.
        _agentColor (str): The color of the agent.
        _heatMapView (bool): Indicates if the heat map view is enabled.
        _heatMapColor (str): The color of the heat map.
        _heatMapBaseColor (str): The base color of the heat map.
        _heatGradient (float): The gradient value for the heat map.
        _startState (tuple): The initial position of the agent.
        _currentPosition (tuple): The current position of the agent.
        _startTime (float): The start time of the agent.
        _endTime (float): The end time of the agent.
        algorithmCallBack (function): Callback function for the agent's algorithm.
    """
    def __init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=True, heatMapColor:str="#FFA732", agentPos:tuple=(0,0), heatGradient:float=0.05):
        if not isinstance(world, CreateGridWorld):
            raise TypeError("World must be an instance of CreateGridWorld!")
        self._worldObj = world
        self._worldID = world.worldID
        self._root = world._root
        self._agentName = agentName
        self._agentColor = agentColor
        self._heatMapView = heatMapView
        self._heatMapColor = heatMapColor
        self._heatMapBaseColor = heatMapColor
        self._heatGradient = heatGradient
        # ~~~~~~~~~~ Agent Position ~~~~~~~~~~ #
        self._startState = agentPos
        self._currentPosition = agentPos
        self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].configure(bg=self._agentColor)
        self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].unbind("<Button-1>")
        self._root.update()
        # ~~~~~~~~~~ Base Heat Map Color ~~~~~~~~~~ #
        if self._heatMapView:
            BR, BG, BB = int(self._heatMapColor[1:3], 16), int(self._heatMapColor[3:5], 16), int(self._heatMapColor[5:7], 16)
            hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
            saturation = 0.1
            BR, BG, BB = colorsys.hsv_to_rgb(hue, saturation, value)
            BR = int(BR*255)
            BG = int(BG*255)
            BB = int(BB*255)
            self._heatMapBaseColor = f"#{BR:02x}{BG:02x}{BB:02x}"
        # ~~~~~~~~~~ Algorithm Call Back Function ~~~~~~~~~~ #
        self.algorithmCallBack = None
        # ~~~~~~~~~~ Agent record ~~~~~~~~~~ #
        self._startTime = time.time()
        self._endTime = None
    
    def __str__(self):
        """
        Describes the attributes of the world.

        Parameters:
            None

        Returns:
            function(): The attributes of the world.
        """
        return self.aboutAgent()

    def aboutAgent(self):
        """
        Prints information about the agent.

        Parameters:
            None

        Returns:
            str: A string containing information about the agent.
        """
        about = PrettyTable()
        about.field_names = ["Attribute", "Value"]
        about.add_row(["Agent Name", self._agentName])
        about.add_row(["Agent Color", self._agentColor])
        about.add_row(["World Name", self._worldObj._worldName])
        about.add_row(["World ID", self._worldID])
        about.add_row(["Start Position", self._startState])
        return str(about)
    
    def summary(self):
        """
        Returns a summary of the agent run.

        Parameters: 
            None
        Returns:
            str: A summary of the agent run.
        """
        summary = PrettyTable()
        summary.field_names = ["Attribute", "Value"]
        summary.add_row(["Start Time", strftime("%a, %d %b %Y %H:%M:%S", gmtime(self._startTime))])
        summary.add_row(["End Time", strftime("%a, %d %b %Y %H:%M:%S", gmtime(self._endTime))])
        summary.add_row(["Elapsed Time", f"{round(self._endTime - self._startTime, 3)} sec"])
        return str(summary)
    
    def setStartState(self, i:int, j:int):
        """
        Sets the start state of the agent to the specified position (i, j).

        Args:
            i (int): The row index of the start position.
            j (int): The column index of the start position.

        Raises:
            ValueError: If the specified start position is invalid.

        """
        if((0 <= i < self._worldObj._rows) and (0 <= j < self._worldObj._cols) and (not self.checkBlockState(i, j))):
            self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].configure(bg=self._worldObj._pathColor)
            self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].bind("<Button-1>", lambda event, i=self._currentPosition[0], j=self._currentPosition[1]: self._worldObj._toggleCell(event, i, j))
            self._startState = (i, j)
            self._currentPosition = self._startState
            self._worldObj._cells[i][j].configure(bg=self._agentColor)
            self._worldObj._cells[i][j].unbind("<Button-1>")
            self._root.update()
        else:
            raise ValueError("Invalid start state!")
    
    def setAlgorithmCallBack(self, algorithmCallBack):
        """
        Set the callback function for the algorithm.

        Parameters:
            algorithmCallBack (function): The callback function to be set.

        Returns:
            None
        """
        self.algorithmCallBack = algorithmCallBack
    
    def runAlgorithm(self):
        """
        Executes the algorithm callback function.
    
        Raises:
            ValueError: If the algorithm callback function is not set.
        """
        if self.algorithmCallBack is None:
            raise ValueError("Algorithm Call Back Function not set!")
        self._worldObj._disableCellToggle()
        self._worldObj._heatMapValueGrid[self._startState[0]][self._startState[1]] += 1
        self._startTime = time.time()
        self.algorithmCallBack()
        self._endTime = time.time()
    
    def _warmerColor(self, color:str, sValue):
        """
        Generates a warmer color from the given color.
        Parameters:
            color (str): The color to be mapped.
            sValue (float): The saturation value.
        
        Returns:
            str: The mapped color.
        """
        # Convert the mapped value to a color
        BR, BG, BB = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        # print(f"BR: {BR}, BG: {BG}, BB: {BB}")
        hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
        # print(f"HSV: {hue}, {saturation}, {value}. sValue {sValue}")
        saturation += sValue
        # print(f"HSV: {hue}, {saturation}, {value}. sValue {sValue}")
        if saturation > 1:
            saturation = 1
        R, G, B = colorsys.hsv_to_rgb(hue, saturation, value)
        R = int(R*255)
        G = int(G*255)
        B = int(B*255)
        return f"#{R:02x}{G:02x}{B:02x}"

    def getHeatMapColor(self, value: float):
        """
        Maps a value to a color on a heat map.

        Args:
            value (float): The value to be mapped.

        Returns:
            tuple: The RGB color tuple representing the mapped value on the heat map.
        """
        # Use exponential decay function to map value to [0, 1]
        mappedValue = 0.9 * (1 - math.exp((-1 * self._heatGradient) * value))  # Adjust the decay constant to change the color gradient
        return self._warmerColor(self._heatMapBaseColor, mappedValue)

    def _updateHeatMap(self, i, j):
        """
        Updates the heat map at the specified position (i, j).

        Parameters:
            i (int): The row index of the position.
            j (int): The column index of the position.
        Returns:
            None
        """
        if(self._heatMapView):
            self._modifyCellColor(i, j, self.getHeatMapColor(self._worldObj._heatMapValueGrid[i][j]))
        else:
            self._modifyCellColor(i, j, self._worldObj._pathColor)

    def _modifyCellColor(self, i, j, color):
        """
        Modify the color of the cell at the specified position (i, j).
        Parameters:
            i (int): The row index of the position.
            j (int): The column index of the position.
        Returns:
            None
        
        """
        self._worldObj._cells[i][j].configure(bg=color)
        self._root.update()

    def checkGoalState(self, i, j):
        """
        Check if the given position (i, j) is a goal state.

        Parameters:
            i (int): The row index of the position.
            j (int): The column index of the position.

        Returns:
            bool: True if the position is a goal state, False otherwise.
        """
        if self._worldObj._world[i][j] == 1:
            return True
        else:
            return False
        
    def checkBlockState(self, i, j):
        """
        Check the state of a block in the world.

        Parameters:
            i (int): The row index of the block.
            j (int): The column index of the block.

        Returns:
            bool: True if the block is empty (-1), False otherwise.
        """
        if self._worldObj._world[i][j] == -1:
            return True
        else:
            return False
        
    def _canMove(self, i, j):
        """
        Check if the agent can move to the specified position (i, j).

        Parameters:
            i (int): The row index of the target position.
            j (int): The column index of the target position.
        
        Returns:
            bool: True if the agent can move to the target position, False otherwise.
        """
        if((0 <= i < self._worldObj._rows) and (0 <= j < self._worldObj._cols) and (not self.checkBlockState(i, j))):
            return True
        else:
            return False

    def moveAgent(self, i, j, delay:float=0.5):
        """
        Moves the agent to the specified position (i, j) on the grid.

        Args:
            i (int): The row index of the target position.
            j (int): The column index of the target position.
            delay (int, optional): The delay in seconds before moving the agent. Defaults to 1.

        Returns:
            bool: True if the agent successfully moves to the target position, False otherwise.
        """
        if(self._canMove(i, j)):
            time.sleep(delay)
            x, y = self._currentPosition
            self._updateHeatMap(x, y)
            self._currentPosition = (i, j)
            self._worldObj._heatMapValueGrid[i][j] += 1
            self._modifyCellColor(i, j, self._agentColor)
            return True
        else:
            return False


# ~~~~~~~~~~~~~~~~ Tree Agent ~~~~~~~~~~~~~~~~ #

class TreeAgent():
    """
    The Tree Agent class.

    Parameters:
        world (CreateTreeWorld): The world object that the agent belongs to.
        agentName (str): The name of the agent.
        agentColor (str, optional): The color of the agent. Defaults to "blue".
        heatMapView (bool, optional): Flag indicating whether to enable heat map view. Defaults to True.
        heatMapColor (str, optional): The color of the heat map. Defaults to "#FFA732".
        heatGradient (float, optional): The gradient of the heat map. Defaults to 0.05.

    Attributes:
        _worldObj (CreateTreeWorld): The tree world object.
        _worldID (str): The ID of the world.
        _root (Tk): The root Tkinter object from the tree world.
        _agentName (str): The name of the agent.
        _agentColor (str): The color of the agent.
        _heatMapView (bool): Indicates if the heat map view is enabled.
        _heatMapColor (str): The color of the heat map.
        _heatMapBaseColor (str): The base color of the heat map.
        _heatGradient (float): The gradient value for the heat map.
        _treeRoot (TreeNode): The root node of the tree.
        _currentNode (TreeNode): The current node the agent is on.
        algorithmCallBack (function): Callback function for the agent's algorithm.
        _startTime (float): The start time of the agent.
        _endTime (float): The end time of the agent.
    """
    def __init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=True, heatMapColor:str="#FFA732", heatGradient:float=0.05):
        if not isinstance(world, CreateTreeWorld):
            raise TypeError("World must be an instance of CreateTreeWorld!")
        self._worldObj = world
        self._worldID = world.worldID
        self._root = world._root
        self._agentName = agentName
        self._agentColor = agentColor
        self._heatMapView = heatMapView
        self._heatMapColor = heatMapColor
        self._heatMapBaseColor = heatMapColor
        self._heatGradient = heatGradient
        # ~~~~~~~~~~ Agent Position ~~~~~~~~~~ #
        self._treeRoot = world.root
        self._worldObj.changeNodeColor(self._treeRoot.id, self._agentColor)
        self._currentNode = self._treeRoot
        # ~~~~~~~~~~ Base Heat Map Color ~~~~~~~~~~ #
        if self._heatMapView:
            BR, BG, BB = int(self._heatMapColor[1:3], 16), int(self._heatMapColor[3:5], 16), int(self._heatMapColor[5:7], 16)
            hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
            saturation = 0.1
            BR, BG, BB = colorsys.hsv_to_rgb(hue, saturation, value)
            BR = int(BR*255)
            BG = int(BG*255)
            BB = int(BB*255)
            self._heatMapBaseColor = f"#{BR:02x}{BG:02x}{BB:02x}"
        # ~~~~~~~~~~ Algorithm Call Back Function ~~~~~~~~~~ #
        self.algorithmCallBack = None
        self._startTime = time.time()
        self._endTime = None
        
    
    def __str__(self):
        """
        Describes the attributes of the world.

        Parameters:
            None

        Returns:
            function(): The attributes of the world.
        """
        return self.aboutAgent()

    def aboutAgent(self):
        """
        Prints information about the agent.

        Parameters:
            None

        Returns:
            str: A string containing information about the agent.
        """
        about = PrettyTable()
        about.field_names = ["Attribute", "Value"]
        about.add_row(["Agent Name", self._agentName])
        about.add_row(["Agent Color", self._agentColor])
        about.add_row(["World Name", self._worldObj._worldName])
        about.add_row(["World ID", self._worldID])
        about.add_row(["Root Node ID", self._treeRoot.id])
        return str(about)

    def summary(self):
        """
        Returns a summary of the agent run.

        Returns:
            str: A summary of the agent run.
        """
        summary = PrettyTable()
        summary.field_names = ["Attribute", "Value"]
        summary.add_row(["Start Time", strftime("%a, %d %b %Y %H:%M:%S", gmtime(self._startTime))])
        summary.add_row(["End Time", strftime("%a, %d %b %Y %H:%M:%S", gmtime(self._endTime))])
        summary.add_row(["Elapsed Time", f"{round(self._endTime - self._startTime, 3)} sec"])
        return str(summary)

    def setAlgorithmCallBack(self, algorithmCallBack):
        """
        Set the callback function for the algorithm.

        Parameters:
            algorithmCallBack (function): The callback function to be set.

        Returns:
            None
        """
        self.algorithmCallBack = algorithmCallBack
    
    def runAlgorithm(self):
            """
            Executes the algorithm callback function.

            Raises:
                ValueError: If the algorithm callback function is not set.
            """
            if self.algorithmCallBack is None:
                raise ValueError("Algorithm Call Back Function not set!")
            self._treeRoot._heatMapValue = 1
            self._startTime = time.time()
            self.algorithmCallBack()
            self._endTime = time.time()
    
    def _warmerColor(self, color:str, sValue):
        """
        Generates a warmer color from the given color.
        Parameters:
            color (str): The color to be mapped.
            sValue (float): The saturation value.
        
        Returns:
            str: The mapped color.
        """
        # Convert the mapped value to a color
        BR, BG, BB = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        # print(f"BR: {BR}, BG: {BG}, BB: {BB}")
        hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
        saturation += sValue
        if saturation > 1:
            saturation = 1
        R, G, B = colorsys.hsv_to_rgb(hue, saturation, value)
        R = int(R*255)
        G = int(G*255)
        B = int(B*255)
        return f"#{R:02x}{G:02x}{B:02x}"


    def getHeatMapColor(self, value: float):
        """
        Returns the color for a given value on a heat map.

        Parameters:
            value (float): The value to map to a color on the heat map.

        Returns:
            tuple: The RGB color value for the given value on the heat map.

        """
        # Use exponential decay function to map value to [0, 1]
        mappedValue = 0.9 * (1 - math.exp((-1 * self._heatGradient) * value))  # Adjust the decay constant to change the color gradient
        return self._warmerColor(self._heatMapBaseColor, mappedValue)

    def _updateHeatMap(self, node):
        if(self._heatMapView):
            self._modifyCellColor(node, self.getHeatMapColor(node._heatMapValue))
        else:
            self._modifyCellColor(node, self._worldObj._nodeColor)

    def _modifyCellColor(self, node, color):
        """
        Modify the color of the cell at the specified position (i, j).
        Parameters:
            i (int): The row index of the position.
            j (int): The column index of the position.
        Returns:
            None
        
        """
        self._worldObj.changeNodeColor(node.id, color)
        self._root.update()

    def checkGoalState(self, nodeId):
        """
        Check if the given node is a goal state.

        Parameters:
        - nodeId: The node Id to be checked.

        Returns:
        - True if the node is a goal state, False otherwise.
        """
        if(nodeId in self._worldObj.nodeMap.keys()):
            node = self._worldObj.getNode(nodeId)
            if(node.isGoalState):
                return True
            else:
                return False
        else:
            return False


    def moveAgent(self, nodeId, delay:int=1):
        """
        Moves the agent to the specified node.

        Args:
            nodeId: The node Id to which the agent should be moved.
            delay (optional): The delay (in seconds) before moving to the next node. Default is 1 second.

        Returns:
            bool: True if the agent was successfully moved to the node, False otherwise.
        """
        if(nodeId in self._worldObj.nodeMap.keys()):
            node = self._worldObj.nodeMap[nodeId]
            time.sleep(delay)
            parent = self._currentNode
            self._updateHeatMap(parent)
            self._currentNode = node
            self._currentNode._heatMapValue += 1
            self._modifyCellColor(node, self._agentColor)
            return True
        else:
            return False
        

# ~~~~~~~~~~~~~~~~ Graph Agent ~~~~~~~~~~~~~~~~ #


class GraphAgent():
    """
    The Graph Agent class.

    Parameters:
        world (CreateGridWorld): The world object that the agent belongs to.
        agentName (str): The name of the agent.
        agentColor (str, optional): The color of the agent. Defaults to "blue".
        heatMapView (bool, optional): Flag indicating whether to enable heat map view. Defaults to True.
        heatMapColor (str, optional): The color of the heat map. Defaults to "#FFA732".
        heatGradient (float, optional): The gradient of the heat map. Defaults to 0.05.

    Attributes:
        _worldObj (CreateGraphWorld): The graph world object.
        _worldID (str): The ID of the world.
        _root (Tk): The root Tkinter object from the graph world.
        _agentName (str): The name of the agent.
        _agentColor (str): The color of the agent.
        _heatMapView (bool): Indicates if the heat map view is enabled.
        _heatMapColor (str): The color of the heat map.
        _heatMapBaseColor (str): The base color of the heat map.
        _heatGradient (float): The gradient value for the heat map.
        _currentNode (GraphNode): The current node the agent is on.
        _startState (GraphNode): The start node of the graph.
        algorithmCallBack (function): Callback function for the agent's algorithm.
        _startTime (float): The start time of the agent.
        _endTime (float): The end time of the agent.
    """
    def __init__(self, world, agentName:str, agentColor:str="blue", startNodeId = None, heatMapView:bool=True, heatMapColor:str="#FFA732", heatGradient:float=0.05):
        if not isinstance(world, CreateGraphWorld):
            raise TypeError("World must be an instance of CreateGraphWorld!")
        self._worldObj = world
        self._worldID = world.worldID
        self._root = world._root
        self._agentName = agentName
        self._agentColor = agentColor
        self._heatMapView = heatMapView
        self._heatMapColor = heatMapColor
        self._heatMapBaseColor = heatMapColor
        self._heatGradient = heatGradient
        # ~~~~~~~~~~ Agent Position ~~~~~~~~~~ #
        if startNodeId is not None:
            self._currentNode = self._worldObj.getNode(startNodeId)
        else:
            self._currentNode = self._worldObj.nodeMap[list(self._worldObj.nodeMap.keys())[0]]
        self._startState = self._currentNode
        self._worldObj.changeNodeColor(self._startState.id, self._agentColor)
        # ~~~~~~~~~~ Base Heat Map Color ~~~~~~~~~~ #
        if self._heatMapView:
            BR, BG, BB = int(self._heatMapColor[1:3], 16), int(self._heatMapColor[3:5], 16), int(self._heatMapColor[5:7], 16)
            hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
            saturation = 0.1
            BR, BG, BB = colorsys.hsv_to_rgb(hue, saturation, value)
            BR = int(BR*255)
            BG = int(BG*255)
            BB = int(BB*255)
            self._heatMapBaseColor = f"#{BR:02x}{BG:02x}{BB:02x}"
        # ~~~~~~~~~~ Algorithm Call Back Function ~~~~~~~~~~ #
        self.algorithmCallBack = None
        self._startTime = time.time()
        self._endTime = None
    
    def __str__(self):
        """
        Describes the attributes of the world.

        Parameters:
            None

        Returns:
            function(): The attributes of the world.
        """
        return self.aboutAgent()

    def aboutAgent(self):
        """
        Prints information about the agent.

        Parameters:
            None

        Returns:
            str: A string containing information about the agent.
        """
        about = PrettyTable()
        about.field_names = ["Attribute", "Value"]
        about.add_row(["Agent Name", self._agentName])
        about.add_row(["Agent Color", self._agentColor])
        about.add_row(["World Name", self._worldObj._worldName])
        about.add_row(["World ID", self._worldID])
        about.add_row(["Start Node ID", self._startState.id])
        return str(about)

    def summary(self):
        """
        Returns a summary of the agent run.

        Parameters: 
            None
        Returns:
            str: A summary of the agent run.
        """
        summary = PrettyTable()
        summary.field_names = ["Attribute", "Value"]
        summary.add_row(["Start Time", strftime("%a, %d %b %Y %H:%M:%S", gmtime(self._startTime))])
        summary.add_row(["End Time", strftime("%a, %d %b %Y %H:%M:%S", gmtime(self._endTime))])
        summary.add_row(["Elapsed Time", f"{round(self._endTime - self._startTime, 3)} sec"])
        return str(summary)
    
    def setStartState(self, nodeId):
        """
        Sets the start state of the agent to the specified node.

        Args:
            nodeId: The ID of the node to set as the start state.

        Raises:
            ValueError: If the specified node ID is invalid.

        """
        if nodeId in self._worldObj._position.keys():
            if self._startState.isGoalState:
                self._worldObj.changeNodeColor(self._startState.id, self._worldObj._goalColor)
            else:
                self._worldObj.changeNodeColor(self._startState.id, self._worldObj._nodeColor)
            self._currentNode = self._worldObj.getNode(nodeId)
            self._startState = self._currentNode
            self._worldObj.root = self._startState
            self._worldObj.changeNodeColor(nodeId, self._agentColor)
        else:
            raise ValueError("Invalid start state!")

    def setAlgorithmCallBack(self, algorithmCallBack):
        """
        Set the callback function for the algorithm.

        Parameters:
        algorithmCallBack (function): The callback function to be set.

        Returns:
        None
        """
        self.algorithmCallBack = algorithmCallBack
    
    def runAlgorithm(self):
        """
        Executes the algorithm callback function.

        Raises:
            ValueError: If the algorithm callback function is not set.
        """
        if self.algorithmCallBack is None:
            raise ValueError("Algorithm Call Back Function not set!")
        self._startState._heatMapValue = 1
        self._startTime = time.time()
        self.algorithmCallBack()
        self._endTime = time.time()
    
    def _warmerColor(self, color:str, sValue):
        """
        Generates a warmer color from the given color.
        Parameters:
            color (str): The color to be mapped.
            sValue (float): The saturation value.
        
        Returns:
            str: The mapped color.
        """
        # Convert the mapped value to a color
        BR, BG, BB = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        # print(f"BR: {BR}, BG: {BG}, BB: {BB}")
        hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
        saturation += sValue
        if saturation > 1:
            saturation = 1
        R, G, B = colorsys.hsv_to_rgb(hue, saturation, value)
        R = int(R*255)
        G = int(G*255)
        B = int(B*255)
        return f"#{R:02x}{G:02x}{B:02x}"


    def getHeatMapColor(self, value: float):
        """
        Returns the color for a given value on a heat map.

        Parameters:
            value (float): The value to map to a color on the heat map.

        Returns:
            tuple: The RGB color value for the given value on the heat map.

        """
        # Use exponential decay function to map value to [0, 1]
        mappedValue = 0.9 * (1 - math.exp((-1 * self._heatGradient) * value))  # Adjust the decay constant to change the color gradient
        return self._warmerColor(self._heatMapBaseColor, mappedValue)

    def _updateHeatMap(self, node):
        """
        Updates the heat map at the specified position (i, j).

        Parameters:
            i (int): The row index of the position.
            j (int): The column index of the position.
        Returns:
            None
        """
        if(self._heatMapView):
            self._modifyCellColor(node, self.getHeatMapColor(node._heatMapValue))
        else:
            self._modifyCellColor(node, self._worldObj._nodeColor)

    def _modifyCellColor(self, node, color):
        self._worldObj.changeNodeColor(node.id, color)
        self._root.update()

    def checkGoalState(self, nodeId):
        """
        Check if the given node is a goal state.

        Parameters:
            node: The ID of the node to be checked.

        Returns:
            bool: True if the node is a goal state, False otherwise.
        """
        if(nodeId in self._worldObj.nodeMap.keys()):
            node = self._worldObj.getNode(nodeId)
            if(node.isGoalState):
                return True
            else:
                return False
        else:
            return False


    def moveAgent(self, nodeId, delay:int=1):
        """
        Moves the agent to the specified node.

        Args:
            nodeId: The ID of the node to which the agent should be moved.
            delay (optional): The delay (in seconds) before moving to the next node. Default is 1 second.

        Returns:
            bool: True if the agent was successfully moved to the node, False otherwise.
        """
        if(nodeId in self._worldObj.nodeMap.keys()):
            node = self._worldObj.nodeMap[nodeId]
            time.sleep(delay)
            parent = self._currentNode
            self._updateHeatMap(parent)
            self._currentNode = node
            self._currentNode._heatMapValue += 1
            self._modifyCellColor(node, self._agentColor)
            return True
        else:
            return False