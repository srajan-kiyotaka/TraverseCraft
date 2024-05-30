from tkinter import *
from tkinter import ttk
from PIL import  ImageTk, Image
from iconHashInfo import IconHashMap
import tkinter.font as font
from typing import List
import threading
import os

class CreateGridWorld:
    """
    """
    setOfCoordinates = List[List[int]]
    coordinate = List[int]
    worldID = "mcWORLD"
    def __init__(self, worldName:str, rows:int, cols:int, cellSize:int=12, pathColor:str="green", blockCode:int=36, blockColor:str="red", goalCode:int=14, goalColor:str="green",cellPadding:int=2, borderWidth:int=2, buttonBgColor:str="#7FC7D9", buttonFgColor:str="#332941", textFont:str="Helvetica", textSize:int=24, textWeight:str="bold", buttonText:str="Start Agent",fullscreen: bool=False):
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
        self._blockCode = blockCode
        self._borderWidth = borderWidth
        self._goalColor = goalColor
        self._goalCells = None
        self._goalCode = goalCode

        # ~~~~~ Button Attributes ~~~~~ #
        self._buttonBgColor = buttonBgColor
        self._buttonFgColor = buttonFgColor
        self._buttonText = buttonText
        self._textFont = textFont
        self._textSize = textSize
        self._textWeight = textWeight
        # ~~~~~ Agent Info ~~~~~ #
        self._agent = None
        # Create an instance of ImageHashMap
        iconHashMap = IconHashMap()
        # Load the image hash map from a file
        iconHashMap.loadFromFile()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, "icons")
        self._blockIconPath = f"{full_path}/{iconHashMap.getName(self._blockCode)}"
        self._blockIcon = Image.open(self._blockIconPath)
        self._blockIcon = self._blockIcon.resize((self._cellSize - self._cellPadding, self._cellSize - self._cellPadding), Image.Resampling.LANCZOS)
        self._goalIconPath = f"{full_path}/{iconHashMap.getName(self._goalCode)}"
        self._goalIcon = Image.open(self._goalIconPath)
        self._goalIcon = self._goalIcon.resize((self._cellSize - self._cellPadding, self._cellSize - self._cellPadding), Image.Resampling.LANCZOS)
        # ~~~~~ World Construction ~~~~~ #
        self._root = Tk()
        self._root.title(self._worldName)
        if fullscreen:
            width= self._root.winfo_screenwidth() 
            height= self._root.winfo_screenheight()
            self._root.geometry("%dx%d" % (width, height))
        else:
            self._root.geometry(f"{self._rows * (self._cellSize + 2*self._cellPadding + 2*self._borderWidth)}x{self._cols * (self._cellSize + 2*self._cellPadding + 2*self._borderWidth)}")
        self._world = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self._cells = [[None for j in range(self._cols)] for i in range(self._rows)]
        self._labelCells = [[None for j in range(self._cols)] for i in range(self._rows)]
        # ~~~~~~ Block Image Generation ~~~~~~ #
        self._blockIcon = ImageTk.PhotoImage(self._blockIcon)
        self._goalIcon = ImageTk.PhotoImage(self._goalIcon)

    def __str__(self):
        return f"World Name: {self._worldName}\nRows: {self._rows}\nCols: {self._cols}\nWindow Size: {self._rows * (self._cellSize + 2*self._cellPadding + 2*self._borderWidth)}x{self._cols * (self._cellSize + 2*self._cellPadding + 2*self._borderWidth)}"

    def constructWorld(self):
        """
        """
        if(self._goalCells is None):
            self._cells[self._rows - 1][self._cols - 1] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._goalColor, borderwidth=self._borderWidth)
            self._labelCells[self._rows - 1][self._cols - 1] = Label(self._cells[self._rows - 1][self._cols - 1], image=self._goalIcon)
            self._labelCells[self._rows - 1][self._cols - 1].pack()
            self._cells[self._rows - 1][self._cols - 1].grid(row=self._rows - 1, column=self._cols - 1, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._root.update()
            self._world[self._rows - 1][self._cols - 1] = 1
        for i in range(self._rows):
            for j in range(self._cols):
                if(self._cells[i][j] is None):
                    self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._pathColor, borderwidth=self._borderWidth)
                    self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
                    self._cells[i][j].bind("<Button-1>", lambda event, i=i, j=j: self.toggleCell(event, i, j))  # Bind left-click event
                    self._root.update()
          # Create a "Start Agent" button
        self._startButton = Button(self._root, text=self._buttonText, command=self._startAgent, bg=self._buttonBgColor, fg=self._buttonFgColor)
        self._startButton['font'] = font.Font(family=self._textFont, size=self._textSize, weight=self._textWeight)
        # self.start_button.pack()
        self._startButton.grid(row=self._rows, column=0, columnspan=self._cols, padx=self._cellPadding, pady=self._cellPadding, sticky="n")
        self._root.update()
    
    def addBlockPath(self, blockCells:list):
        """
        """
        self._blockCells = blockCells
        for i, j in self._blockCells:
            self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._blockColor, borderwidth=self._borderWidth)
            self._labelCells[i][j] = Label(self._cells[i][j], image=self._blockIcon)
            self._labelCells[i][j].bind("<Button-1>", lambda event, i=i, j=j: self.toggleCell(event, i, j))
            self._labelCells[i][j].pack()
            self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._cells[i][j].bind("<Button-1>", lambda event, i=i, j=j: self.toggleCell(event, i, j))  # Bind left-click event
            self._root.update()
            self._world[i][j] = -1
        print(self._blockIcon)

    
    def addGoalState(self, goalState:setOfCoordinates):
        """
        """
        self._goalCells = goalState
        for i, j in self._goalCells:
            self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._goalColor, borderwidth=self._borderWidth)
            self._labelCells[i][j] = Label(self._cells[i][j], image=self._goalIcon)
            self._labelCells[i][j].pack()
            self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._root.update()
            self._world[i][j] = 1
    
    
    def updateWorld(self):
        """
        """
        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
                self._root.update()
    
    def toggleCell(self, event, i, j):
        """
        """
        # print(f"Cell: {i}, {j}: {self._world[i][j]}")
        if self._world[i][j] == 0:
            self._cells[i][j].configure(bg=self._blockColor)
            if(self._labelCells[i][j] is None):
                self._labelCells[i][j] = Label(self._cells[i][j], image=self._blockIcon)
                self._labelCells[i][j].bind("<Button-1>", lambda event, i=i, j=j: self.toggleCell(event, i, j))
            self._labelCells[i][j].pack()
            self._root.update()
            self._world[i][j] = -1
        else:
            self._cells[i][j].configure(bg=self._pathColor)
            self._labelCells[i][j].pack_forget()
            self._root.update()
            self._world[i][j] = 0
    
    # Agent block
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
        """
        """

        self._root.mainloop()

    def printWorld(self):
        """
        """
        print(self._worldName)
        print(self._world)

# class CreateTreeWorld:
    

# class CreateGraphWorld:


# world = CreateGridWorld("Grid Test Run", rows = 15, cols = 15, cellSize = 50)
# world.addBlockPath([[0,0],[1,1],[4,2],[7,3],[8,4],[2,5],[9,6],[2,7]])
# world.constructWorld()
# # world.printWorld()
# print(world)
# world.showWorld()