from tkinter import *
from tkinter import ttk

class CreateGridWorld:
    """
    """
    def __init__(self, worldName:str, rows:int, cols:int, cellSize:int=10, cellColor:str="white", cellPadding:int=2, borderWidth:int=1):
        # ~~~~~ World Attributes ~~~~~ #
        self._worldName = worldName
        self._rows = rows
        self._cols = cols
        self._world = None
        self._blockCells = None
        # ~~~~~ Cell Attributes ~~~~~ #
        self._cellSize = cellSize
        self._cellColor = cellColor
        self._cellPadding = cellPadding
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
                    self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg="green", borderwidth=self._borderWidth)

        # Add cells to the grid using the Grid geometry manager
        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)

    def blockPath(self, blockCells:list):
        """
        """
        self._blockCells = blockCells
        for i in range(len(self._blockCells)):
            self._cells[self._blockCells[i][0]][self._blockCells[i][1]] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg="red", borderwidth=self._borderWidth)
            self._world[self._blockCells[i][0]][self._blockCells[i][1]] = -1

    def showWorld(self):
        self._root.mainloop()

    def printWorld(self):
        print(self._worldName)
        print(self._world)

# class CreateTreeWorld:
class CreateTreeWorld:
    def __init__(self, worldName: str, rows: int, cols: int, cellSize: int = 10, cellColor: str = "white", cellPadding: int = 2, borderWidth: int = 1):
        # ~~~~~ World Attributes ~~~~~ #
        self._worldName = worldName
        self._rows = rows
        self._cols = cols
        self._world = None
        self._treeCells = None
        # ~~~~~ Cell Attributes ~~~~~ #
        self._cellSize = cellSize
        self._cellColor = cellColor
        self._cellPadding = cellPadding
        self._borderWidth = borderWidth
        self.cells = None
        # ~~~~~ Cell Styles ~~~~~ #
        # Add any additional cell styles specific to trees if needed
        # self._cellStyles = ttk.Style()
        # self._cellStyles.configure("Tree.TFrame", background="brown") #, borderwidth=self._borderWidth)
        # ~~~~~ World Construction ~~~~~ #
        self._root = Tk()
        self._root.title(self._worldName)
        self._root.geometry(f"{self._rows * (self._cellSize + 2*self._cellPadding)}x{self._cols * (self._cellSize + 2*self._cellPadding)}")
        self._world = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self._cells = [[None for j in range(self._cols)] for i in range(self._rows)]

    def __str__(self):
        return f"World Name: {self._worldName}\nRows: {self._rows}\nCols: {self._cols}\nWindow Size: {self._rows * (self._cellSize + self._cellPadding)}x{self._cols * (self._cellSize + self._cellPadding)}"

    def constructWorld(self):
        for i in range(self._rows):
            for j in range(self._cols):
                if self._cells[i][j] is None:
                    # Modify cell creation as needed for trees
                    self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg="brown", borderwidth=self._borderWidth)

        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)

    def blockPath(self, blockCells: list):
        self._blockCells = blockCells
        for i in range(len(self._blockCells)):
            row, col = self._blockCells[i]
            self._cells[row][col] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg="green", borderwidth=self._borderWidth)
            self._world[row][col] = -1
    def showWorld(self):
        self._root.mainloop()
    
    def printWorld(self):
        print(self._worldName)
        print(self._world)
    

# class CreateGraphWorld:


# world = CreateGrudWorld("Grid Test Run", rows = 10 , cols = 10, cellSize = 50, cellColor = "gray")
# world.blockPath([[0,0],[1,1],[4,2],[7,3],[8,4],[2,5],[9,6],[2,7]])
# world.constructWorld()
# world.printWorld()
# print(world)
# world.showWorld()

world = CreateTreeWorld("Tree Test Run", rows=10, cols=10, cellSize=50, cellColor="gray")
world.blockPath([[0, 0], [1, 1], [4, 2], [7, 3], [8, 4], [2, 5], [9, 6], [2, 7]])
world.constructWorld()
world.printWorld()
print(world)
world.showWorld()