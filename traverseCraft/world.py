from tkinter import *
from tkinter import ttk
from typing import List
import tkinter.font as font
from .dataStructures import TreeNode
import threading
import platform
import math
import subprocess


def getScreenSize():
    try:
        os_type = platform.system()
        print(f"OS Type: {os_type}")
        return _getScreenSizeWindow()
    except:
        raise NotImplementedError(f"Unsupported OS: {os_type}")

def _getScreenSizeWindow():
    root = Tk()
    root.withdraw()  # Hide the root window
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height


global SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_WIDTH, SCREEN_HEIGHT = getScreenSize()


class CreateGridWorld:
    """
    """
    setOfCoordinates = List[List[int]]
    coordinate = List[int]
    worldID = "GRIDWORLD"
    def __init__(self, worldName:str, rows:int, cols:int, cellSize:int=10, pathColor:str="gray", blockColor:str="red", goalColor:str="green", cellPadding:int=2, borderWidth:int=1, buttonBgColor:str="#7FC7D9", buttonFgColor:str="#332941", textFont:str="Helvetica", textSize:int=24, textWeight:str="bold", buttonText:str="Start Agent"):
        # ~~~~~ World Attributes ~~~~~ #
        self._worldName = worldName
        self._rows = rows
        self._cols = cols
        self._world = None
        self._blockCells = None
        # ~~~~~ Cell Attributes ~~~~~ #
        self._cellSize = cellSize
        self._pathColor = pathColor
        self._cellPadding = cellPadding
        self._blockColor = blockColor
        self._borderWidth = borderWidth
        self._goalColor = goalColor
        self._goalCells = None
        # ~~~~~ Button Attributes ~~~~~ #
        self._buttonBgColor = buttonBgColor
        self._buttonFgColor = buttonFgColor
        self._buttonText = buttonText
        self._textFont = textFont
        self._textSize = textSize
        self._textWeight = textWeight
        # ~~~~~ Agent Info ~~~~~ #
        self._agent = None
        # ~~~~~ Cell Styles ~~~~~ #
        # self._cellStyles = ttk.Style()
        # self._cellStyles.configure("Path.TFrame", background="green") #, borderwidth=self._borderWidth)
        # self._cellStyles.configure("Block.TFrame", background="red") #, borderwidth=self._borderWidth)
        # ~~~~~ World Construction ~~~~~ #
        self._root = Tk()
        self._root.title(self._worldName)
        self._root.geometry(f"{(self._rows) * (self._cellSize + 2*self._cellPadding)}x{(self._cols + 1) * (self._cellSize + 2*self._cellPadding)}")
        self._world = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self._cells = [[None for j in range(self._cols)] for i in range(self._rows)]

    def __str__(self):
        return f"World Name: {self._worldName}\nRows: {self._rows}\nCols: {self._cols}\nWindow Size: {(self._rows) * (self._cellSize + 2*self._cellPadding)}x{(self._cols + 1) * (self._cellSize + 2*self._cellPadding)}"

    def constructWorld(self):
        """
        """
        if(self._goalCells is None):
            self._cells[self._rows - 1][self._cols - 1] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._goalColor, borderwidth=self._borderWidth)
            self._cells[self._rows - 1][self._cols - 1].grid(row=self._rows - 1, column=self._cols - 1, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._root.update()
            self._world[self._rows - 1][self._cols - 1] = 1

        for i in range(self._rows):
            for j in range(self._cols):
                if(self._cells[i][j] is None):
                    self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._pathColor, borderwidth=self._borderWidth)
                    self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
                    self._cells[i][j].bind("<Button-1>", lambda event, i=i, j=j: self._toggleCell(event, i, j))  # Bind left-click event
                    self._root.update()
        
        # Create a "Start Agent" button
        self._startButton = Button(self._root, text=self._buttonText, command=self._startAgent, bg=self._buttonBgColor, fg=self._buttonFgColor)
        self._startButton['font'] = font.Font(family=self._textFont, size=self._textSize, weight=self._textWeight)
        # self.start_button.pack()
        self._startButton.grid(row=self._rows, column=0, columnspan=self._cols, padx=self._cellPadding, pady=self._cellPadding, sticky="n")
        self._root.update()

    def _startAgent(self):
        """
        """
        self._startButton.configure(state=DISABLED)
        self._root.update()
        if(self._agent is None):
            raise ValueError("Agent not set!")
        agentThread = threading.Thread(target=self._agent.runAlgorithm, args=())
        agentThread.start()

    # def GridAgentRun(self, agent):
    #     """
    #     """
    #     raise NotImplementedError("GridAgentRun() must be implemented in the agent class!")

    def addBlockPath(self, blockCells:setOfCoordinates):
        """
        """
        self._blockCells = blockCells
        for i, j in self._blockCells:
            self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._blockColor, borderwidth=self._borderWidth)
            self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._cells[i][j].bind("<Button-1>", lambda event, i=i, j=j: self._toggleCell(event, i, j))  # Bind left-click event
            self._root.update()
            self._world[i][j] = -1


    def addGoalState(self, goalState:setOfCoordinates):
        """
        """
        self._goalCells = goalState
        for i, j in self._goalCells:
            self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._goalColor, borderwidth=self._borderWidth)
            self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._root.update()
            self._world[i][j] = 1

    def setAgent(self, agent):
        """
        """
        self._agent = agent
 
    def updateWorld(self):
        """
        """
        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
                self._root.update()
    
    def _toggleCell(self, event, i, j):
        """
        """
        if self._world[i][j] == 0:
            self._cells[i][j].configure(bg=self._blockColor)
            self._root.update()
            self._world[i][j] = -1
        else:
            self._cells[i][j].configure(bg=self._pathColor)
            self._root.update()
            self._world[i][j] = 0


    def showWorld(self):
        """
        """
        self._root.mainloop()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Tree World ~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class CreateTreeWorld:
    worldID = "TREEWORLD"
    def __init__(self, worldName: str, worldInfo: dict, radius: int = 20, fontSize:int=12, fontBold:bool = True, fontItalic:bool = True, nodeColor: str = "gray", rootColor: str="red", goalColor: str="green", width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT, lineThickness: int =2, arrowShape: tuple = (10, 12, 5)):
        self._worldName = worldName
        # check important parameters in world info #
        if "root" not in worldInfo:
            raise ValueError("World info is missing 'root' key")
        if "goals" not in worldInfo:
            raise ValueError("World info is missing 'goals' key")
        if "adj" not in worldInfo:
            raise ValueError("World info is missing 'adj' key")
        if "position" not in worldInfo:
            raise ValueError("World info is missing 'position' key")
        ############################################
        self._worldInfo = worldInfo
        self._treeRootId = worldInfo["root"]
        self._goalIds = worldInfo["goals"]
        self._position = worldInfo["position"]
        self._width = width
        self._height = height
        # self.currentNode = self._treeRoot
        self._radius = radius
        self._nodeColor = nodeColor
        self._rootColor = rootColor
        self._goalColor = goalColor
        self._fontSize = fontSize
        self._fontBold = fontBold
        self._fontItalic = fontItalic
        self._lineThickness = lineThickness
        self._arrowShape = arrowShape
        self._root = Tk()
        self._root.title(self._worldName)
        self._canvas = Canvas(self._root, width=self._width, height=self._height, bg="white")
        self._canvas.pack()
        self.root = None
        ## Construct Tree Data Structure ##
        if("edges" not in self._worldInfo):
            self._worldInfo['edges'] = None
        if("vals" not in self._worldInfo):
            self._worldInfo['vals'] = None
        self.root = self._generateTreeDS(self._worldInfo["adj"], self._treeRootId, self._worldInfo["edges"], self._worldInfo['vals'])
        # Agent information #
        self._agent = None

    def __str__(self):
        return f"World Name: {self._worldName}\nNode Radius: {self._radius}\nWindow Size: {self._height}x{self._width}"

    def _generateTreeDS(self, adj, rootId, edges=None, values=None):
        if rootId not in adj:
            raise ValueError(f"Root ID {rootId} not found in adjacency list")
        elif adj[rootId] is None or len(adj[rootId]) == 0:
            return TreeNode(rootId, children=[], edges=[], isGoalState=(rootId in self._goalIds))
        
        children = []
        for childId in adj[rootId]:
            children.append(self._generateTreeDS(adj, childId))
        
        if(edges is not None):
            if(values is not None):
                return TreeNode(rootId, values=[rootId], children=children, edges=edges[rootId], isGoalState=(rootId in self._goalIds))
            else:
                return TreeNode(rootId, children=children, edges=edges[rootId], isGoalState=(rootId in self._goalIds))
        else:
            if(values is not None):
                return TreeNode(rootId, values=[rootId], children=children, edges=[], isGoalState=(rootId in self._goalIds))
                            
        return TreeNode(rootId, children=children, edges=[], isGoalState=(rootId in self._goalIds))

    def constructWorld(self):
        self._constructWorld()

    def _constructWorld(self):
        self._drawNodeEdges(self.root)

    def _drawNodeEdges(self, node):
        if node is None:
            return
        
        node_id = node.id
        x, y = self._position[node_id]

        # Determine the color based on the node type
        color = self._nodeColor
        if node_id == self._treeRootId:
            color = self._rootColor
        elif node_id in self._goalIds:
            color = self._goalColor

        # Draw the node
        self._canvas.create_oval(x - self._radius, y - self._radius, x + self._radius, y + self._radius, fill=color)

        # Draw the node value
        font_style = ("Helvetica", self._fontSize, "bold italic" if self._fontBold and self._fontItalic else "bold" if self._fontBold else "italic" if self._fontItalic else "normal")
        self._canvas.create_text(x, y, text=str(node_id), font=font_style, fill="black")

        # Draw the edges and recursively draw the children nodes
        for i, child in enumerate(node.children):
            child_id = child.id
            child_x, child_y = self._position[child_id]

            # Calculate the angle for the line
            angle = math.atan2(child_y - y, child_x - x)
            start_x = x + self._radius * math.cos(angle)
            start_y = y + self._radius * math.sin(angle)
            end_x = child_x - self._radius * math.cos(angle)
            end_y = child_y - self._radius * math.sin(angle)

            # Draw the edge
            self._canvas.create_line(start_x, start_y, end_x, end_y, width=self._lineThickness, arrow=LAST, arrowshape=self._arrowShape)

            # Recursively draw the child node
            self._drawNodeEdges(child)

    def setAgent(self, agent):
        """
        """
        self._agent = agent
    
    def _startAgent(self):
        """
        """
        self._startButton.configure(state=DISABLED)
        self._root.update()
        if(self._agent is None):
            raise ValueError("Agent not set!")
        agentThread = threading.Thread(target=self._agent.runAlgorithm, args=())
        agentThread.start()

    def showWorld(self):
        self._root.mainloop()
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Test Code ~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~ Grid World ~~~~~ #
# world = CreateGridWorld("Grid Test Run", rows = 20, cols = 20, cellSize = 40)
# world.addBlockPath([[0,0],[1,1],[4,2],[7,3],[8,4],[2,5],[9,6],[2,7]])
# world.constructWorld()
# # world.printWorld()
# print(world)
# world.showWorld()
        
# ~~~~~ Tree World ~~~~~ #
# Example tree structure
