from tkinter import *
from tkinter import ttk
from typing import List
import tkinter.font as font
from .dataStructures import TreeNode, GraphNode
import threading
import platform
import math
import os
import subprocess
from prettytable import PrettyTable


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
    Class representing a grid world.

    Attributes:
        setOfCoordinates (List[List[int]]): A list of coordinates.
        coordinate (List[int]): A list representing a coordinate.
        worldID (str): The ID of the world.

    Args:
        worldName (str): The name of the world.
        rows (int): The number of rows in the world.
        cols (int): The number of columns in the world.
        cellSize (int, optional): The size of each cell in pixels. Defaults to 10.
        pathColor (str, optional): The color of the path cells. Defaults to "gray".
        blockColor (str, optional): The color of the block cells. Defaults to "red".
        goalColor (str, optional): The color of the goal cells. Defaults to "green".
        cellPadding (int, optional): The padding around each cell in pixels. Defaults to 2.
        borderWidth (int, optional): The width of the cell borders in pixels. Defaults to 1.
        buttonBgColor (str, optional): The background color of the button. Defaults to "#7FC7D9".
        buttonFgColor (str, optional): The foreground color of the button. Defaults to "#332941".
        textFont (str, optional): The font of the button text. Defaults to "Helvetica".
        textSize (int, optional): The size of the button text. Defaults to 24.
        textWeight (str, optional): The weight of the button text. Defaults to "bold".
        buttonText (str, optional): The text displayed on the button. Defaults to "Start Agent".
    """
    setOfCoordinates = List[List[int]]
    coordinate = List[int]
    worldID = "GRIDWORLD"
    def __init__(self, worldName:str, rows:int, cols:int, cellSize:int=10, pathColor:str="gray", blockColor:str="red", goalColor:str="green", cellPadding:int=2, borderWidth:int=1, buttonBgColor:str="#7FC7D9", buttonFgColor:str="#332941", textFont:str="Helvetica", textSize:int=24, textWeight:str="bold", buttonText:str="Start Agent", logoPath:str=None):
        # ~~~~~ World Attributes ~~~~~ #
        self._worldName = worldName
        self._rows = rows
        self._cols = cols
        self._world = None
        self._blockCells = None
        self._logoPath = logoPath
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, "icons")
        full_path = os.path.join(full_path, "logo")
        full_path = os.path.join(full_path, "design 1.png")
        if self._logoPath is None:
            self._logoPath = full_path
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
        self._setWindowIcon(self._logoPath)
        self._root.geometry(f"{(self._rows) * (self._cellSize + 2*self._cellPadding)}x{(self._cols + 1) * (self._cellSize + 2*self._cellPadding)}")
        self._world = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self._cells = [[None for j in range(self._cols)] for i in range(self._rows)]
        self._heatMapValueGrid = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def __str__(self):
        return self.aboutWorld()

    def _setWindowIcon(self, logoPath):
        icon = PhotoImage(file=logoPath)
        self._root.iconphoto(False, icon)
    
    def aboutWorld(self):
        """
        Generates a summary of the world.

        Returns:
        - str: The summary of the world.
        """
        about = PrettyTable()
        about.field_names = ["Attribute", "Value"]
        about.add_row(["World Name", self._worldName])
        about.add_row(["Rows", self._rows])
        about.add_row(["Columns", self._cols])
        about.add_row(["Cell Size", self._cellSize])
        about.add_row(["Cell Padding", self._cellPadding])
        about.add_row(["Window Size", f"{(self._rows) * (self._cellSize + 2*self._cellPadding)}x{(self._cols + 1) * (self._cellSize + 2*self._cellPadding)}"])
        about.add_row(["Path Color", self._pathColor])
        about.add_row(["Block Color", self._blockColor])
        about.add_row(["Goal Color", self._goalColor])
        about.add_row(["Border Width", self._borderWidth])
        about.add_row(["Button Background Color", self._buttonBgColor])
        about.add_row(["Button Foreground Color", self._buttonFgColor])
        about.add_row(["Button Text", self._buttonText])
        about.add_row(["Text Font", self._textFont])
        about.add_row(["Text Size", self._textSize])
        about.add_row(["Text Weight", self._textWeight])
        return str(about)

    def summary(self):
        """
        Generates a summary of the world.

        Returns:
        - str: The summary of the world.
        """
        summary = PrettyTable()
        columns = ['Cell'] + [f"{i}" for i in range(self._cols)]
        summary.field_names = columns
        for i in range(self._rows):
            row = [f"{i}"]
            for j in range(self._cols):
                row.append(self._heatMapValueGrid[i][j])
            summary.add_row(row)
        return str(summary)

    def constructWorld(self):
        """
        Constructs the world by creating and arranging cells in the GUI.
        If the goal cells are not set, it creates a goal cell at the bottom-right corner of the grid.
        It also creates cells for each row and column in the grid, and binds a left-click event to toggle the cells.
        Finally, it creates a "Start Agent" button at the bottom of the grid.

        Parameters:
            None

        Returns:
            None
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
        self._startButton.configure(state=DISABLED)
        self._root.update()
        if(self._agent is None):
            raise ValueError("Agent not set!")
        agentThread = threading.Thread(target=self._agent.runAlgorithm, args=())
        agentThread.start()


    def addBlockPath(self, blockCells:setOfCoordinates):
        """
        Adds block cells to the world grid.

        Parameters:
        - blockCells (setOfCoordinates): A set of coordinates representing the block cells.

        Returns:
        - None

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
        Adds the goal state to the world grid.

        Parameters:
        - goalState (setOfCoordinates): A set of coordinates representing the goal state.

        Returns:
        None
        """
        self._goalCells = goalState
        for i, j in self._goalCells:
            self._cells[i][j] = Frame(self._root, width=self._cellSize, height=self._cellSize, bg=self._goalColor, borderwidth=self._borderWidth)
            self._cells[i][j].grid(row=i, column=j, sticky="nsew", padx=self._cellPadding, pady=self._cellPadding)
            self._root.update()
            self._world[i][j] = 1

    def setAgent(self, agent):
        """
        Set the agent for the world.

        Parameters:
        agent (Agent): The agent object to set.

        Returns:
        None
        """
        self._agent = agent
 
    def updateWorld(self):
        """
        Updates the world by positioning the cells in a grid layout and updating the root window.

        This method iterates over each cell in the world and positions it in a grid layout using the row and column indices.
        It also updates the root window to reflect any changes made to the world.

        Note:
        - The cells are positioned using the `grid` method with the specified row and column indices.
        - The `sticky` parameter is set to "nsew" to make the cells stick to all sides of their respective grid cells.
        - The `padx` and `pady` parameters specify the padding around each cell.

        Returns:
        None
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


    def _disableCellToggle(self):
        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].unbind("<Button-1>")
    
    def showWorld(self):
        """
        Displays the world.
        """
        self._root.mainloop()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Tree World ~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class CreateTreeWorld:
    """
        Class representing a tree world.

        Parameters:
        - worldName (str): The name of the world.
        - worldInfo (dict): A dictionary containing information about the world.
        - radius (int): The radius of the nodes in the world visualization. Default is 20.
        - fontSize (int): The font size of the node labels. Default is 12.
        - fontBold (bool): Whether to use bold font for the node labels. Default is True.
        - fontItalic (bool): Whether to use italic font for the node labels. Default is True.
        - nodeColor (str): The color of the nodes. Default is "gray".
        - rootColor (str): The color of the root node. Default is "red".
        - goalColor (str): The color of the goal nodes. Default is "green".
        - width (int): The width of the world visualization canvas. Default is SCREEN_WIDTH.
        - height (int): The height of the world visualization canvas. Default is SCREEN_HEIGHT.
        - lineThickness (int): The thickness of the lines connecting the nodes. Default is 2.
        - arrowShape (tuple): The shape of the arrows indicating the direction of the edges. Default is (10, 12, 5).
        - buttonBgColor (str): The background color of the buttons. Default is "#7FC7D9".
        - buttonFgColor (str): The foreground color of the buttons. Default is "#332941".
        - textFont (str): The font family of the button text. Default is "Helvetica".
        - textSize (int): The font size of the button text. Default is 24.
        - textWeight (str): The font weight of the button text. Default is "bold".
        - buttonText (str): The text displayed on the buttons. Default is "Start Agent".
        """
    worldID = "TREEWORLD"
    def __init__(self, worldName: str, worldInfo: dict, radius: int = 20, fontSize:int=12, fontBold:bool = True, fontItalic:bool = True, nodeColor: str = "gray", rootColor: str="red", goalColor: str="green", width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT, lineThickness: int =2, arrowShape: tuple = (10, 12, 5), buttonBgColor:str="#7FC7D9", buttonFgColor:str="#332941", textFont:str="Helvetica", textSize:int=24, textWeight:str="bold", buttonText:str="Start Agent", logoPath:str=None):
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
        self._radius = radius
        self._nodeColor = nodeColor
        self._rootColor = rootColor
        self._goalColor = goalColor
        self._fontSize = fontSize
        self._fontBold = fontBold
        self._fontItalic = fontItalic
        self._lineThickness = lineThickness
        self._arrowShape = arrowShape
        self._logoPath = logoPath
        if self._logoPath is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(script_dir, "icons")
            full_path = os.path.join(full_path, "logo")
            full_path = os.path.join(full_path, "design 1.png")
            self._logoPath = full_path
        self._root = Tk()
        self._root.title(self._worldName)
        self._setWindowIcon(self._logoPath)
        self._canvas = Canvas(self._root, width=self._width, height=self._height, bg="white")
        self._canvas.pack()
        self.root = None
        ## Construct Tree Data Structure ##
        self.nodeMap = {nodeId : None for nodeId in self._worldInfo["position"].keys()}
        if("edges" not in self._worldInfo):
            self._worldInfo['edges'] = None
        if("vals" not in self._worldInfo):
            self._worldInfo['vals'] = None
        self.root = self._generateTreeDS(self._worldInfo["adj"], self._treeRootId, self._worldInfo["edges"], self._worldInfo['vals'])
        # ~~~~~ Agent information ~~~~~ #
        self._agent = None
        self._nodeObj = {}
        self._nodeTextObj = {}
        # ~~~~~ Button Attributes ~~~~~ #
        self._buttonBgColor = buttonBgColor
        self._buttonFgColor = buttonFgColor
        self._buttonText = buttonText
        self._textFont = textFont
        self._textSize = textSize
        self._textWeight = textWeight

    def __str__(self):
        return self.aboutWorld()

    def _setWindowIcon(self, logoPath):
        icon = PhotoImage(file=logoPath)
        self._root.iconphoto(False, icon)
    
    def aboutWorld(self):
        """
        Generates a summary of the world.

        Returns:
            str: The summary of the world.
        """
        about = PrettyTable()
        about.field_names = ["Attribute", "Value"]
        about.add_row(["World Name", self._worldName])
        about.add_row(["Root Node ID", self._treeRootId])
        about.add_row(["Goal Nodes", self._goalIds])
        about.add_row(["Width", self._width])
        about.add_row(["Height", self._height])
        about.add_row(["Node Radius", self._radius])
        about.add_row(["Font Size", self._fontSize])
        about.add_row(["Font Bold", self._fontBold])
        about.add_row(["Font Italic", self._fontItalic])
        about.add_row(["Node Color", self._nodeColor])
        about.add_row(["Goal Color", self._goalColor])
        about.add_row(["Line Thickness", self._lineThickness])
        about.add_row(["Arrow Shape", self._arrowShape])
        about.add_row(["Button Background Color", self._buttonBgColor])
        about.add_row(["Button Foreground Color", self._buttonFgColor])
        about.add_row(["Text Font", self._textFont])
        about.add_row(["Text Size", self._textSize])
        about.add_row(["Text Weight", self._textWeight])
        about.add_row(["Button Text", self._buttonText])
        return str(about)

    def summary(self):
        """
        Generates a summary of the world.

        Returns:
            str: The summary of the world.
        """
        summary = PrettyTable()
        summary.field_names = ['Node ID', 'Number of Visits'] 
        for nodeId, node in self.nodeMap.items():
            summary.add_row([nodeId, node._heatMapValue])
        return str(summary)

    def _generateTreeDS(self, adj, rootId, edges=None, values=None):
        if rootId not in adj:
            raise ValueError(f"Root ID {rootId} not found in adjacency list")
        elif adj[rootId] is None or len(adj[rootId]) == 0:
            self.nodeMap[rootId] = TreeNode(rootId, children=[], edges=[], isGoalState=(rootId in self._goalIds))
            return self.nodeMap[rootId]
        
        children = []
        for childId in adj[rootId]:
            children.append(self._generateTreeDS(adj, childId, edges, values))
        
        if(edges is not None):
            if(values is not None):
                self.nodeMap[rootId] = TreeNode(rootId, values=values[rootId], children=children, edges=edges[rootId], isGoalState=(rootId in self._goalIds))
            else:
                self.nodeMap[rootId] = TreeNode(rootId, children=children, edges=edges[rootId], isGoalState=(rootId in self._goalIds))
        else:
            if(values is not None):
                self.nodeMap[rootId] = TreeNode(rootId, values=values[rootId], children=children, edges=[], isGoalState=(rootId in self._goalIds))
            else:
                self.nodeMap[rootId] = TreeNode(rootId, children=children, edges=[], isGoalState=(rootId in self._goalIds))

        return self.nodeMap[rootId]
    
    def constructWorld(self):
        """
        Constructs the tree world.

        Parameters:
            self (World): The World instance.

        Returns:
            None
        """
        self._constructWorld()

    def _constructWorld(self):
        self._drawEdges(self.root)
        self._drawNodes(self.root)
        self._addStartButton()

    def _drawNodes(self, node):
        if node is None:
            return
        
        nodeId = node.id
        x, y = self._position[nodeId]

        # Determine the color based on the node type
        color = self._nodeColor
        if nodeId == self._treeRootId:
            color = self._rootColor
        elif nodeId in self._goalIds:
            color = self._goalColor

        # Draw the node
        self._nodeObj[nodeId] = self._canvas.create_oval(x - self._radius, y - self._radius, x + self._radius, y + self._radius, fill=color)

        # Draw the node value
        font_style = ("Helvetica", self._fontSize, "bold italic" if self._fontBold and self._fontItalic else "bold" if self._fontBold else "italic" if self._fontItalic else "normal")
        self._nodeTextObj[nodeId] = self._canvas.create_text(x, y, text=str(nodeId), font=font_style, fill="black")

        # Recursively draw the children nodes
        for i, child in enumerate(node.children):
            # Recursively draw the child node
            self._drawNodes(child)

    def _drawEdges(self, node):
        if node is None:
            return
        
        nodeId = node.id
        x, y = self._position[nodeId]

        # Draw the edges and recursively draw the children edges
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
            self._drawEdges(child)


    def _addStartButton(self):
        # Find the bottommost point of the tree
        button_y = 100 + max(y for _, y in self._position.values())
        button_x = (min(x for x, _ in self._position.values()) + max(x for x, _ in self._position.values())) // 2

        # Create the "Start Agent" button
        self._startButton = Button(self._root, text=self._buttonText, command=self._startAgent, bg=self._buttonBgColor, fg=self._buttonFgColor)
        self._startButton['font'] = font.Font(family=self._textFont, size=self._textSize, weight=self._textWeight)
        self._startButton.place(x=button_x, y=button_y, anchor="center")
    
    def changeNodeColor(self, nodeId, color):
        """
        Changes the color of a node in the tree.

        Args:
            nodeId (int): The ID of the node to change the color of.
            color (str): The new color to set for the node.

        Returns:
            None
        """
        if nodeId in self._nodeObj:
            self._canvas.itemconfig(self._nodeObj[nodeId], fill=color)

    def changeNodeText(self, nodeId, newText):
        if nodeId in self._nodeTextObj:
            self._canvas.itemconfig(self._nodeTextObj[nodeId], text=newText)
    
    def getNode(self, nodeId):
        """
        Returns the pointer to the node with the given nodeId.

        Parameters:
            nodeId: The ID of the node to retrieve the pointer for.

        Returns:
            Node: The pointer to the node with the given nodeId.
        """
        return self.nodeMap[nodeId]
    
    def setAgent(self, agent):
        """
        Set the agent for the world.

        Parameters:
        agent (Agent): The agent to be set.

        Returns:
        None
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
        Displays the world.
        """
        self._root.mainloop()
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Graph World ~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class CreateGraphWorld:
    """
        Class representing a graph world.

        Parameters:
        - worldName (str): The name of the world.
        - worldInfo (dict): A dictionary containing information about the world.
        - radius (int): The radius of the nodes in the world visualization. Default is 20.
        - fontSize (int): The font size of the node labels. Default is 12.
        - fontBold (bool): Whether to use bold font for the node labels. Default is True.
        - fontItalic (bool): Whether to use italic font for the node labels. Default is True.
        - nodeColor (str): The color of the nodes. Default is "gray".
        - rootColor (str): The color of the root node. Default is "red".
        - goalColor (str): The color of the goal nodes. Default is "green".
        - width (int): The width of the world visualization canvas. Default is SCREEN_WIDTH.
        - height (int): The height of the world visualization canvas. Default is SCREEN_HEIGHT.
        - lineThickness (int): The thickness of the lines connecting the nodes. Default is 2.
        - arrowShape (tuple): The shape of the arrows indicating the direction of the edges. Default is (10, 12, 5).
        - buttonBgColor (str): The background color of the buttons. Default is "#7FC7D9".
        - buttonFgColor (str): The foreground color of the buttons. Default is "#332941".
        - textFont (str): The font family of the button text. Default is "Helvetica".
        - textSize (int): The font size of the button text. Default is 24.
        - textWeight (str): The font weight of the button text. Default is "bold".
        - buttonText (str): The text displayed on the buttons. Default is "Start Agent".
        """
    worldID = "GRAPHWORLD"
    def __init__(self, worldName: str, worldInfo: dict, radius: int = 20, fontSize:int=12, fontBold:bool = True, fontItalic:bool = True, nodeColor: str = "gray", rootColor: str="red", goalColor: str="green", width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT, lineThickness: int =2, arrowShape: tuple = (10, 12, 5), buttonBgColor:str="#7FC7D9", buttonFgColor:str="#332941", textFont:str="Helvetica", textSize:int=24, textWeight:str="bold", buttonText:str="Start Agent", logoPath:str=None):
        self._worldName = worldName
        # check important parameters in world info #
        if "goals" not in worldInfo:
            raise ValueError("World info is missing 'goals' key")
        if "adj" not in worldInfo:
            raise ValueError("World info is missing 'adj' key")
        if "position" not in worldInfo:
            raise ValueError("World info is missing 'position' key")
        ############################################
        self._worldInfo = worldInfo
        self._graphRootId = list(worldInfo["position"].keys())[0]
        self._goalIds = worldInfo["goals"]
        self._position = worldInfo["position"]
        self._width = width
        self._height = height
        self._radius = radius
        self._nodeColor = nodeColor
        self._goalColor = goalColor
        self._fontSize = fontSize
        self._fontBold = fontBold
        self._fontItalic = fontItalic
        self._lineThickness = lineThickness
        self._arrowShape = arrowShape
        self._logoPath = logoPath
        if self._logoPath is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(script_dir, "icons")
            full_path = os.path.join(full_path, "logo")
            full_path = os.path.join(full_path, "design 1.png")
            self._logoPath = full_path
        self._root = Tk()
        self._root.title(self._worldName)
        self._setWindowIcon(self._logoPath)
        self._canvas = Canvas(self._root, width=self._width, height=self._height, bg="white")
        self._canvas.pack()
        self.nodeMap = {}
        ## Construct Tree Data Structure ##
        if("edges" not in self._worldInfo):
            self._worldInfo['edges'] = None
        if("vals" not in self._worldInfo):
            self._worldInfo['vals'] = None
        self._visited = {nodeId: False for nodeId in self._worldInfo["position"].keys()}
        self.root = self._generateGraphDS(self._worldInfo["adj"], self._graphRootId, None, self._worldInfo["edges"], self._worldInfo['vals'], visited=self._visited)
        # ~~~~~ Agent information ~~~~~ #
        self._agent = None
        self._nodeObj = {}
        self._nodeTextObj = {}
        # ~~~~~ Button Attributes ~~~~~ #
        self._buttonBgColor = buttonBgColor
        self._buttonFgColor = buttonFgColor
        self._buttonText = buttonText
        self._textFont = textFont
        self._textSize = textSize
        self._textWeight = textWeight

    def __str__(self):
        return self.aboutWorld()

    def _setWindowIcon(self, logoPath):
        icon = PhotoImage(file=logoPath)
        self._root.iconphoto(False, icon)

    def aboutWorld(self):
        """
        Generates a summary of the world.

        Returns:
            str: The summary of the world.
        """
        about = PrettyTable()
        about.field_names = ["Attribute", "Value"]
        about.add_row(["World Name", self._worldName])
        about.add_row(["Goal Nodes", self._goalIds])
        about.add_row(["Width", self._width])
        about.add_row(["Height", self._height])
        about.add_row(["Node Radius", self._radius])
        about.add_row(["Font Size", self._fontSize])
        about.add_row(["Font Bold", self._fontBold])
        about.add_row(["Font Italic", self._fontItalic])
        about.add_row(["Node Color", self._nodeColor])
        about.add_row(["Goal Color", self._goalColor])
        about.add_row(["Line Thickness", self._lineThickness])
        about.add_row(["Arrow Shape", self._arrowShape])
        about.add_row(["Button Background Color", self._buttonBgColor])
        about.add_row(["Button Foreground Color", self._buttonFgColor])
        about.add_row(["Text Font", self._textFont])
        about.add_row(["Text Size", self._textSize])
        about.add_row(["Text Weight", self._textWeight])
        about.add_row(["Button Text", self._buttonText])
        return str(about)

    def summary(self):
        """
        Generates a summary of the world.

        Returns:
            str: The summary of the world.
        """
        summary = PrettyTable()
        summary.field_names = ['Node ID', 'Number of Visits'] 
        for nodeId, node in self.nodeMap.items():
            summary.add_row([nodeId, node._heatMapValue])
        return str(summary)

    def _generateGraphDS(self, adj, rootId, parentId=None, edges=None, values=None, visited={}):
        if rootId not in adj:
            raise ValueError(f"Root ID {rootId} not found in adjacency list")
        
        if visited[rootId]:
            return None
        
        visited[rootId] = True

        if (adj[rootId] is None or len(adj[rootId]) == 0) or (parentId is not None and len(adj[rootId]) == 1 and adj[rootId][0] == parentId):
            self.nodeMap[rootId] = GraphNode(rootId, neighbors=[], edges=[], isGoalState=(rootId in self._goalIds))
            return self.nodeMap[rootId]
        
        for neighId in adj[rootId]:
            if visited[neighId] or (parentId is not None and neighId == parentId):
                continue
            else:
                self.nodeMap[neighId] = self._generateGraphDS(adj, neighId, rootId, edges, values, visited)
        
        if(edges is not None):
            if(values is not None):
                self.nodeMap[rootId] = GraphNode(rootId, values=values[rootId], neighbors=adj[rootId], edges=edges[rootId], isGoalState=(rootId in self._goalIds))
            else:
                self.nodeMap[rootId] = GraphNode(rootId, neighbors=adj[rootId], edges=edges[rootId], isGoalState=(rootId in self._goalIds))
        else:
            if(values is not None):
                self.nodeMap[rootId] = GraphNode(rootId, values=values[rootId], neighbors=adj[rootId], edges=[], isGoalState=(rootId in self._goalIds))
            else:
                self.nodeMap[rootId] = GraphNode(rootId, neighbors=adj[rootId], edges=[], isGoalState=(rootId in self._goalIds))

        return self.nodeMap[rootId]

    def constructWorld(self):
        """
        Constructs the tree world.

        Parameters:
            self (World): The World instance.

        Returns:
            None
        """
        self._constructWorld()

    def _constructWorld(self):
        self._drawEdges(self.root)
        self._drawNodes(self.root)
        self._addStartButton()

    def _drawEdges(self, node):
        if node is None:
            return
        
        if not self._visited[node.id]:
            return
        
        nodeId = node.id
        
        self._visited[nodeId] = False

        self.nodeMap[nodeId].neighbors = [self.nodeMap[neighId] for neighId in node.neighbors]

        x, y = self._position[nodeId]

        # Draw the edges and recursively draw the children edges
        for i, neigh in enumerate(node.neighbors):
            neighId = neigh.id
            neigh_x, neigh_y = self._position[neighId]

            # Calculate the angle for the line
            angle = math.atan2(neigh_y - y, neigh_x - x)
            start_x = x + self._radius * math.cos(angle)
            start_y = y + self._radius * math.sin(angle)
            end_x = neigh_x - self._radius * math.cos(angle)
            end_y = neigh_y - self._radius * math.sin(angle)

            # Draw the edge
            self._canvas.create_line(start_x, start_y, end_x, end_y, width=self._lineThickness, arrow=LAST, arrowshape=self._arrowShape)

            # Recursively draw the neigh node
            if self._visited[neighId]:
                self._drawEdges(neigh)

    def _drawNodes(self, node):
        if node is None:
            return
        
        if self._visited[node.id]:
            return
        
        nodeId = node.id
        
        self._visited[nodeId] = True

        x, y = self._position[nodeId]

        # Determine the color based on the node type
        color = self._nodeColor
        if nodeId in self._goalIds:
            color = self._goalColor

        # Draw the node
        self._nodeObj[nodeId] = self._canvas.create_oval(x - self._radius, y - self._radius, x + self._radius, y + self._radius, fill=color)

        # Draw the node value
        font_style = ("Helvetica", self._fontSize, "bold italic" if self._fontBold and self._fontItalic else "bold" if self._fontBold else "italic" if self._fontItalic else "normal")
        self._nodeTextObj[nodeId] = self._canvas.create_text(x, y, text=str(nodeId), font=font_style, fill="black")

        # Recursively draw the children nodes
        for i, neigh in enumerate(node.neighbors):
            neighId = neigh.id

            # Recursively draw the neigh node
            if not self._visited[neighId]:
                self._drawNodes(neigh)

    def _addStartButton(self):
        # Find the bottommost point of the tree
        button_y = 100 + max(y for _, y in self._position.values())
        button_x = (min(x for x, _ in self._position.values()) + max(x for x, _ in self._position.values())) // 2

        # Create the "Start Agent" button
        self._startButton = Button(self._root, text=self._buttonText, command=self._startAgent, bg=self._buttonBgColor, fg=self._buttonFgColor)
        self._startButton['font'] = font.Font(family=self._textFont, size=self._textSize, weight=self._textWeight)
        self._startButton.place(x=button_x, y=button_y, anchor="center")
    
    def changeNodeColor(self, nodeId, color):
        """
        Changes the color of a node in the tree.

        Args:
            nodeId (int): The ID of the node to change the color of.
            color (str): The new color to set for the node.

        Returns:
            None
        """
        if nodeId in self._nodeObj:
            self._canvas.itemconfig(self._nodeObj[nodeId], fill=color)
        else:
            raise ValueError(f"Node ID {nodeId} not found in the graph world!")

    def changeNodeText(self, nodeId, newText):
        if nodeId in self._nodeTextObj:
            self._canvas.itemconfig(self._nodeTextObj[nodeId], text=newText)
        else:
            raise ValueError(f"Node ID {nodeId} not found in the graph world!")
    
    def getNode(self, nodeId):
        """
        Returns the pointer to the node with the given nodeId.

        Parameters:
            nodeId: The ID of the node to retrieve the pointer for.

        Returns:
            Node: The pointer to the node with the given nodeId.
        """
        if nodeId not in self.nodeMap:
            raise ValueError(f"Node ID {nodeId} not found in the graph world!")
        return self.nodeMap[nodeId]
    
    def setAgent(self, agent):
        """
        Set the agent for the world.

        Parameters:
            agent (Agent): The agent to be set.

        Returns:
            None
        """
        self._agent = agent
    
    def _startAgent(self):
        self._startButton.configure(state=DISABLED)
        self._root.update()
        if(self._agent is None):
            raise ValueError("Agent not set!")
        agentThread = threading.Thread(target=self._agent.runAlgorithm, args=())
        agentThread.start()

    def showWorld(self):
        """
        Displays the world.
        """
        self._root.mainloop()
