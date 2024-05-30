from tkinter import *
from tkinter import ttk
from typing import List
import tkinter.font as font
from dataStructures import TreeNode
import threading
import platform


def get_screen_size():
    os_type = platform.system()
    if os_type == 'Windows':
        return get_screen_size_windows()
    elif os_type == 'Linux':
        return get_screen_size_linux()
    elif os_type == 'Darwin':
        return get_screen_size_mac()
    else:
        raise NotImplementedError(f"Unsupported OS: {os_type}")

def get_screen_size_windows():
    import ctypes
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return width, height

def get_screen_size_linux():
    import subprocess
    output = subprocess.check_output(['xrandr']).decode('utf-8')
    for line in output.split('\n'):
        if '*' in line:
            resolution = line.split()[0]
            width, height = map(int, resolution.split('x'))
            return width, height

def get_screen_size_mac():
    import Quartz
    main_display_id = Quartz.CGMainDisplayID()
    width = Quartz.CGDisplayPixelsWide(main_display_id)
    height = Quartz.CGDisplayPixelsHigh(main_display_id)
    return width, height


global SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_size()


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
    worldID = "TREEWORLD"
    setOfCoordinates = List[List[int]]
    def __init__(self, worldName: str, array:setOfCoordinates, radius: int = 36, fontSize:int=12, fontBold:bool = True, fontItalic:bool = True, nodeColor: str = "gray", rootColor: str="red", goalColor: str="green", width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT, lineThickness: int =2, arrowShape: tuple = (15, 17, 8)):
        self._worldName = worldName
        self._treeRoot = self.create_tree(array)
        self._width = width
        self._height = height
        self.currentNode = self._treeRoot
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
    def create_tree(self,arr:setOfCoordinates):
        if not arr:
            return None
        
        root = TreeNode(arr[0][0])
        queue = [root]
        level = 1

        while queue and level < len(arr):
            level_nodes = queue[:]
            queue = []
            
            for node in level_nodes:
                children_values = arr[level]
                left_val = children_values.pop(0) if children_values else None
                right_val = children_values.pop(0) if children_values else None
                
                if left_val is not None:
                    node.left = TreeNode(left_val)
                    queue.append(node.left)
                if right_val is not None:
                    node.right = TreeNode(right_val)
                    queue.append(node.right)
            
            level += 1
        
        return root

    def __str__(self):
        return f"World Name: {self._worldName}\nNode Radius: {self._radius}\nWindow Size: {self._height}x{self._width}"

    def constructWorld(self):
        self._constructWorld(self._treeRoot, self._width // 2, 50, self._width // 4)

    def _constructWorld(self, root, x, y, dx):
        if root is None:
            return
        
        if root.left is not None:
            left_child_x, left_child_y = x - dx, y + 100
            self._canvas.create_line(x - self._radius, y, left_child_x + self._radius, left_child_y - self._radius, arrow=LAST, width=self._lineThickness)
            self._constructWorld(root.left, left_child_x, left_child_y, dx // 2)
        
        if root.right is not None:
            right_child_x, right_child_y = x + dx, y + 100
            self._canvas.create_line(x + self._radius, y, right_child_x - self._radius, right_child_y - self._radius, arrow=LAST, width=self._lineThickness)
            self._constructWorld(root.right, right_child_x, right_child_y, dx // 2)

        node_color = self._rootColor if root == self._treeRoot else self._nodeColor
        self._canvas.create_oval(x - self._radius, y - self._radius, x + self._radius, y + self._radius, fill=node_color, outline="black")
        font_style = ("Helvetica", self._fontSize, ("bold italic" if self._fontBold and self._fontItalic else "bold" if self._fontBold else "italic" if self._fontItalic else ""))
        self._canvas.create_text(x, y, text=root.val, font=font_style)

    def showWorld(self):
        self._root.mainloop()
    
    def printWorld(self):
        print(self._worldName)




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
arr = [[1], [2,3], [4,5,6], [7,8,9,10],[None,1,2,3,4,5]]

tree_world = CreateTreeWorld("Binary Tree Visualization", arr)
tree_world.constructWorld()
tree_world.showWorld()