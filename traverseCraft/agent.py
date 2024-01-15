from world import CreateGridWorld, CreateTreeWorld, TreeNode
from tkinter import Frame, Tk
import time
import math
import colorsys

# Note: we have to make different agents for different worlds.

class GridAgent():
    """
    """
    def __init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=True, heatMapBaseColor:str="#3D3B40", agentPos:tuple=(0,0), heatGradient:int=7):
        """
        """
        if not isinstance(world, CreateGridWorld):
            raise TypeError("World must be an instance of CreateGridWorld!")
        self._worldObj = world
        self._worldID = world.worldID
        self._root = world._root
        self._agentName = agentName
        self._agentColor = agentColor
        self._heatMapView = heatMapView
        self._heatMapBaseColor = heatMapBaseColor
        self._heatMapValueGrid = [[0.0 for _ in range(self._worldObj._cols)] for _ in range(self._worldObj._rows)]
        self._heatGradient = heatGradient
        # ~~~~~~~~~~ Agent Position ~~~~~~~~~~ #
        self._currentPosition = agentPos
        self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].configure(bg=self._agentColor)
        self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].unbind("<Button-1>")
        self._root.update()
    
    def __str__(self):
        return f"Agent Name: {self._agentName}\nAgent Color: {self._agentColor}\nWorld Name: {self._world._worldName}\nWorld ID: {self._worldID}"

    def startState(self, i:int, j:int):
        """
        """
        if((0 <= i < self._worldObj._rows) and (0 <= j < self._worldObj._cols) and (not self.checkBlockState(i, j))):
            self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].configure(bg=self._worldObj._pathColor)
            self._worldObj._cells[self._currentPosition[0]][self._currentPosition[1]].bind("<Button-1>", lambda event, i=self._currentPosition[0], j=self._currentPosition[1]: self._worldObj._toggleCell(event, i, j))
            self._currentPosition = (i, j)
            self._worldObj._cells[i][j].configure(bg=self._agentColor)
            self._worldObj._cells[i][j].unbind("<Button-1>")
            self._root.update()
        else:
            raise ValueError("Invalid start state!")
    
    def getHeatMapColor(self, value:float):
        # Use exponential decay function to map value to [0, 1]
        mappedValue = math.exp((-1 * self._heatGradient) * value)  # Adjust the decay constant to change the color gradient

        # Convert the mapped value to a color
        BR, BG, BB = int(self._heatMapBaseColor[1:3], 16), int(self._heatMapBaseColor[3:5], 16), int(self._heatMapBaseColor[5:7], 16)
        print(f"BR: {BR}, BG: {BG}, BB: {BB}")
        hue, saturation, value = colorsys.rgb_to_hsv(BR, BG, BB)
        hue += value
        if hue > 360:
            hue = 360
        R, G, B = colorsys.hsv_to_rgb(hue, saturation, value)
        R = int(R)
        G = int(G)
        B = int(B)
        print(f"R: {R}, G: {G}, B: {B}")
        # R = int(baseColorRGB[0] * (1 - mappedValue))
        # G = int(baseColorRGB[1] * (1 - mappedValue))
        # B = int(baseColorRGB[2] * (mappedValue))

        return f"#{R:02x}{G:02x}{B:02x}"

    def _updateHeatMap(self, i, j):
        """
        """
        if(self._heatMapView):
            self._heatMapValueGrid[i][j] += 1
            self._modifyCellColor(i, j, self.getHeatMapColor(self._heatMapValueGrid[i][j]))

    def _modifyCellColor(self, i, j, color):
        print(f"({i}, {j}): {color}, value: {self._heatMapValueGrid[i][j]}")
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

    def moveAgent(self, i, j, delay:int=2):
        """
        """
        if(self._canMove(i, j)):
            time.sleep(delay)
            x, y = self._currentPosition
            self._updateHeatMap(x, y)
            self._currentPosition = (i, j)
            self._modifyCellColor(i, j, self._agentColor)
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

