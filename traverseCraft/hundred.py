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
        """Creates the world's visualization, including cells and the start button."""

        # Combine cell creation and event binding for efficiency
        for i in range(self._rows):
            for j in range(self._cols):
                if self._cells[i][j] is None:
                    cell = Frame(
                        self._root,
                        width=self._cellSize,
                        height=self._cellSize,
                        bg=self._pathColor,
                        borderwidth=self._borderWidth,
                    )
                    cell.grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
                    cell.bind("<Button-1>", lambda event, i=i, j=j: self._toggleCell(event, i, j))
                    self._cells[i][j] = cell

        # Handle goal cell separately if needed
        if self._goalCells is None:
            goal_cell = Frame(
                self._root,
                width=self._cellSize,
                height=self._cellSize,
                bg=self._goalColor,
                borderwidth=self._borderWidth,
            )
            goal_cell.grid(row=self._rows - 1, column=self._cols - 1, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._cells[self._rows - 1][self._cols - 1] = goal_cell
            self._world[self._rows - 1][self._cols - 1] = 1

        # Create start button with optimized font handling
        self._startButton = Button(
            self._root,
            text=self._buttonText,
            command=self._startAgent,
            bg=self._buttonBgColor,
            fg=self._buttonFgColor,
            font=("", self._textSize, self._textWeight),  # Optimized font creation
        )
        self._startButton.grid(
            row=self._rows, column=0, columnspan=self._cols, padx=self._cellPadding, pady=self._cellPadding, sticky="n"
        )

        # Update the GUI once after all elements are created
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



# Example usage:
# world = CreateGridWorld("MyWorld", 50, 50)
# world.constructWorld()
# world.showWorld()