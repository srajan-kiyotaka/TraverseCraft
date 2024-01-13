from world import CreateGridWorld, CreateTreeWorld, TreeNode
from tkinter import Frame, Tk
import time
import math

# Note: we have to make different agents for different worlds.

class GridAgent():
    """
    """
    def __init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=False, heatMapBaseColor:str="#FF9843", agentPos:tuple=(0,0)):
        """
        """
        self._worldObj = world
        self._worldID = world.worldID
        self._root = world._root
        self._agentName = agentName
        self._agentColor = agentColor
        self._heatMapView = heatMapView
        self._heatMapBaseColor = heatMapBaseColor
        self._heatMapValueGrid = [[0.0 for _ in range(self._world._cols)] for _ in range(self._world._rows)]
        self._currentPosition = agentPos
    
    def __str__(self):
        return f"Agent Name: {self._agentName}\nAgent Color: {self._agentColor}\nWorld Name: {self._world._worldName}\nWorld ID: {self._worldID}"

    def startState(self, i:int, j:int):
        """
        """
        self._currentPosition = (i, j)
        self._worldObj._cells[i][j].configure(bg=self._agentColor)
        self._root.update()
    
    def getHeatMapColor(self, value:float):
        # Use exponential decay function to map value to [0, 1]
        mappedValue = 1 - math.exp(-5 * value)  # Adjust the decay constant to change the color gradient

        # Convert the mapped value to a color
        baseColorRGB = int(self._heatMapBaseColor[1:3], 16), int(self._heatMapBaseColor[3:5], 16), int(self._heatMapBaseColor[5:7], 16)

        R = int(baseColorRGB[0] * (1 - mappedValue))
        G = int(baseColorRGB[1] * (1 - mappedValue))
        B = int(baseColorRGB[2] * mappedValue)

        return f"#{R:02X}{G:02X}{B:02X}"

    def _updateHeatMap(self, i, j):
        """
        """
        if(self._heatMapView):
            self._heatMapValueGrid[i][j] += 1
            self._modifyCellColor(i, j, self.getHeatMapColor(self._heatMapValueGrid[i][j]))

    def _modifyCellColor(self, i, j, color):
        self._worldObj._cells[i][j].configure(bg=color)
        self._root.update()

    def checkGoalState(self, i, j):
        """
        """
        if(self._worldObj._world[i][j] == 1):
            return True
        else:
            return False
        
    def checkBlockState(self, i, j):
        """
        """
        if(self._worldObj._world[i][j] == -1):
            return True
        else:
            return False
        
    def _canMove(self, i, j):
        """
        """
        if((0 <= i < self._worldObj._rows) and (0 <= j < self._worldObj._cols) and (not self.checkBlockState(i, j))):
            return True
        else:
            return False

    def moveAgent(self, i, j, delay:int=5):
        """
        """
        if(self._canMove(i, j)):
            x, y = self._currentPosition
            self._updateHeatMap(x, y)
            self._currentPosition = (i, j)
            self._modifyCellColor(i, j, self._agentColor)
            time.sleep(delay)
            return True
        else:
            return False


# agent_world = Agent("Agent Test Run", rows=30, cols=30, cellSize=20,agentPos=[2,2])
# agent_world.constructWorld()
# agent_world.addBlockPath([[0, 0], [1, 1], [4, 2], [7, 3], [8, 4], [2, 5], [9, 6], [2, 7]])
# agent_world.modifyCellColor(*agent_world._currentPosition, "blue")
# agent_world.animateMove(agent_world.moveRight, steps=12)
# agent_world.animateMove(agent_world.moveDown, steps=12)
# agent_world.animateMove(agent_world.moveUp, steps=12)
# agent_world.animateMove(agent_world.moveLeft, steps=12)
# agent_world.showWorld()

