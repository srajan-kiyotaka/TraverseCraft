from tkinter import *
from tkinter import ttk

class CreateGridWorld:
    """
    """
    def __init__(self, worldName:str, rows:int, cols:int, cellSize:int=10, pathColor:str="green", blockColor:str="red", cellPadding:int=2, borderWidth:int=1):
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
        self.cells = None
        # ~~~~~ Cell Styles ~~~~~ #
        # self._cellStyles = ttk.Style()
        # self._cellStyles.configure("Path.TFrame", background="green") #, borderwidth=self._borderWidth)
        # self._cellStyles.configure("Block.TFrame", background="red") #, borderwidth=self._borderWidth)
        # ~~~~~ World Construction ~~~~~ #
        self._root = Tk()
        self._root.title(self._worldName)
        self._root.geometry(f"{self._rows * (self._cellSize + 2*self._cellPadding)}x{self._cols * (self._cellSize + 2*self._cellPadding)}")
        self._world = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self._cells = [[None for j in range(self._cols)] for i in range(self._rows)]

    def __str__(self):
        return f"World Name: {self._worldName}\nRows: {self._rows}\nCols: {self._cols}\nWindow Size: {self._rows * (self._cellSize + self._cellPadding)}x{self._cols * (self._cellSize + self._cellPadding)}"

    def constructWorld(self):
        """
        """
        for i in range(self._rows):
            for j in range(self._cols):
                if(self._cells[i][j] is None):
                    self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._pathColor, borderwidth=self._borderWidth)
                    self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
                    self._root.update()


    def blockPath(self, blockCells:list):
        """
        """
        self._blockCells = blockCells
        for i, j in self._blockCells:
            self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._blockColor, borderwidth=self._borderWidth)
            self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._root.update()
            self._world[i][j] = -1

    def updateWorld(self):
        """
        """
        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
                self._root.update()
    
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


world = CreateGridWorld("Grid Test Run", rows = 20, cols = 20, cellSize = 40)
world.blockPath([[0,0],[1,1],[4,2],[7,3],[8,4],[2,5],[9,6],[2,7]])
world.constructWorld()
world.printWorld()
print(world)
world.showWorld()