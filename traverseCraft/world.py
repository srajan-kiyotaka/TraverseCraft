from tkinter import *
from tkinter import ttk
from typing import List
import tkinter.font as font
from dataStructures import TreeNode
import threading

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

    def printWorld(self):
        """
        """
        print(self._worldName)
        print(self._world)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Tree World ~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class CreateTreeWorld:
    """
    """
    worldID = "TREEWORLD"
    def __init__(self, worldName: str, treeRoot, radius: int = 36, fontSize:int=12, fontBold:bool = True, fontItalic:bool = True, nodeColor: str = "gray", rootColor: str="red", goalColor: str="green", width: int = 600, height: int = 400, lineThickness: int =2, arrowShape: tuple = (15, 17, 8)):
        self._worldName = worldName
        # ~~~~~ World Attributes ~~~~~ #
        self._treeRoot = treeRoot
        self._width = width
        self._height = height
        self.currentNode = self._treeRoot
        # ~~~~~ Node Attributes ~~~~~ #
        self._radius = radius
        self._nodeColor = nodeColor
        self._rootColor = rootColor
        self._goalColor = goalColor
        self._fontSize = fontSize
        self._fontBold = fontBold
        self._fontItalic = fontItalic
        # ~~~~~ Cell Styles ~~~~~ #
        self._lineThickness = lineThickness
        self._arrowShape = arrowShape
        # ~~~~~ World Construction ~~~~~ #
        self._root = Tk()
        self._root.title(self._worldName)
        self._canvas = Canvas(self._root, width=600, height=400)
        self._canvas.pack()

    def __str__(self):
        return f"World Name: {self._worldName}\nNode Radius: {self._radius}\nWindow Size: {self._height}x{self._width}"

    def constructWorld(self):
        """
        """
        self._constructWorld(self._treeRoot)

    def _constructWorld(self, root):
        if root.parent is not None:
            parentX, parentY = root.parent.x, root.parent.y
            rootX, rootY = root.x, root.y
            self._canvas.create_line(parentX , (parentY + self._radius), rootX, (rootY - self._radius), width=self._lineThickness, arrow=LAST, arrowshape=self._arrowShape)
        if root.isGoalState:
            self._canvas.create_oval(root.x - self._radius, root.y - self._radius, root.x + self._radius, root.y + self._radius, width=self._lineThickness, fill=self._goalColor)
        elif root.parent is None:
            self._canvas.create_oval(root.x - self._radius, root.y - self._radius, root.x + self._radius, root.y + self._radius, width=self._lineThickness, fill=self._rootColor)
        else:
            self._canvas.create_oval(root.x - self._radius, root.y - self._radius, root.x + self._radius, root.y + self._radius, width=self._lineThickness, fill=self._nodeColor)
        if self._fontBold and self._fontItalic:
            self._canvas.create_text(root.x, root.y, text=root.nodeName, font=("Helvetica", self._fontSize, "bold", "italic"))
        elif self._fontBold:
            self._canvas.create_text(root.x, root.y, text=root.nodeName, font=("Helvetica", self._fontSize, "bold"))
        elif self._fontItalic:
            self._canvas.create_text(root.x, root.y, text=root.nodeName, font=("Helvetica", self._fontSize, "italic"))
        else:
            self._canvas.create_text(root.x, root.y, text=root.nodeName, font=("Helvetica", self._fontSize))

        for child in root.children:
            self._constructWorld(child)

    def showWorld(self):
        self._root.mainloop()
    
    def printWorld(self):
        print(self._worldName)
        # print(self._world)
    



# class CreateGraphWorld:


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
# tree_root = TreeNode("Root", 300, 50)
# child1 = TreeNode("Child 1", 200, 150, tree_root)
# child2 = TreeNode("Child 2", 400, 150, tree_root)
# child3 = TreeNode("Child 3", 150, 250, child1)
# child4 = TreeNode("Child 4", 250, 250, child1, True)

# tree_root.children.extend([child1, child2])
# child1.children.extend([child3, child4])
# world = CreateTreeWorld("Tree Test Run", tree_root)
# world.constructWorld()
# world.showWorld()