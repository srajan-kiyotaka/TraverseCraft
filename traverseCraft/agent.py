from world import CreateGridWorld, CreateTreeWorld, TreeNode
# from hundred import CreateGridWorld
from tkinter import Frame, Tk
import time
import math
import colorsys

# Note: we have to make different agents for different worlds.

class GridAgent():
    """
    """
    def __init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=True, heatMapColor:str="#FFA732", agentPos:tuple=(0,0), heatGradient:float=0.05):
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
        self._heatMapColor = heatMapColor
        self._heatMapBaseColor = heatMapColor
        self._heatMapValueGrid = [[0.0 for _ in range(self._worldObj._cols)] for _ in range(self._worldObj._rows)]
        self._heatGradient = heatGradient
        # ~~~~~~~~~~ Agent Position ~~~~~~~~~~ #
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
    
    def __str__(self):
        return f"Agent Name: {self._agentName}\nAgent Color: {self._agentColor}\nWorld Name: {self._worldObj._worldName}\nWorld ID: {self._worldID}"

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
    
    def setAlgorithmCallBack(self, algorithmCallBack):
        """
        """
        self.algorithmCallBack = algorithmCallBack
    
    def runAlgorithm(self):
        """
        """
        if self.algorithmCallBack is None:
            raise ValueError("Algorithm Call Back Function not set!")
        self.algorithmCallBack()
    
    def _warmerColor(self, color:str, sValue):
        """
        """
        # Convert the mapped value to a color
        BR, BG, BB = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        # print(f"BR: {BR}, BG: {BG}, BB: {BB}")
        hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
        print(f"HSV: {hue}, {saturation}, {value}. sValue {sValue}")
        saturation += sValue
        print(f"HSV: {hue}, {saturation}, {value}. sValue {sValue}")
        if saturation > 1:
            saturation = 1
        R, G, B = colorsys.hsv_to_rgb(hue, saturation, value)
        R = int(R*255)
        G = int(G*255)
        B = int(B*255)
        return f"#{R:02x}{G:02x}{B:02x}"

    def getHeatMapColor(self, value:float):
        """
        """
        # Use exponential decay function to map value to [0, 1]
        mappedValue = 0.9*(1 - math.exp((-1 * self._heatGradient) * value))  # Adjust the decay constant to change the color gradient
        print(mappedValue)
        return self._warmerColor(self._heatMapBaseColor, mappedValue)

    def _updateHeatMap(self, i, j):
        """
        """
        if(self._heatMapView):
            self._heatMapValueGrid[i][j] += 1
            self._modifyCellColor(i, j, self.getHeatMapColor(self._heatMapValueGrid[i][j]))

    def _modifyCellColor(self, i, j, color):
        """
        """
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

    def moveAgent(self, i, j, delay:int=1):
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


class TreeAgent():
    """
    """
    def __init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=True, heatMapColor:str="#FFA732", heatGradient:float=0.05):
        """
        """
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
        self._heatMapValueGrid = [[0.0 for _ in range(self._worldObj._cols)] for _ in range(self._worldObj._rows)]
        self._heatGradient = heatGradient
        # ~~~~~~~~~~ Agent Position ~~~~~~~~~~ #
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
    
    def __str__(self):
        return f"Agent Name: {self._agentName}\nAgent Color: {self._agentColor}\nWorld Name: {self._worldObj._worldName}\nWorld ID: {self._worldID}"

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
    
    def setAlgorithmCallBack(self, algorithmCallBack):
        """
        """
        self.algorithmCallBack = algorithmCallBack
    
    def runAlgorithm(self):
        """
        """
        if self.algorithmCallBack is None:
            raise ValueError("Algorithm Call Back Function not set!")
        self.algorithmCallBack()
    
    def _warmerColor(self, color:str, sValue):
        """
        """
        # Convert the mapped value to a color
        BR, BG, BB = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        # print(f"BR: {BR}, BG: {BG}, BB: {BB}")
        hue, saturation, value = colorsys.rgb_to_hsv(BR/255, BG/255, BB/255)
        print(f"HSV: {hue}, {saturation}, {value}. sValue {sValue}")
        saturation += sValue
        print(f"HSV: {hue}, {saturation}, {value}. sValue {sValue}")
        if saturation > 1:
            saturation = 1
        R, G, B = colorsys.hsv_to_rgb(hue, saturation, value)
        R = int(R*255)
        G = int(G*255)
        B = int(B*255)
        return f"#{R:02x}{G:02x}{B:02x}"

    def getHeatMapColor(self, value:float):
        """
        """
        # Use exponential decay function to map value to [0, 1]
        mappedValue = 0.9*(1 - math.exp((-1 * self._heatGradient) * value))  # Adjust the decay constant to change the color gradient
        print(mappedValue)
        return self._warmerColor(self._heatMapBaseColor, mappedValue)

    def _updateHeatMap(self, i, j):
        """
        """
        if(self._heatMapView):
            self._heatMapValueGrid[i][j] += 1
            self._modifyCellColor(i, j, self.getHeatMapColor(self._heatMapValueGrid[i][j]))

    def _modifyCellColor(self, i, j, color):
        """
        """
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

    def moveAgent(self, i, j, delay:int=1):
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